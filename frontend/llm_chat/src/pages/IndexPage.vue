<template>
  <q-page class="flex flex-center">
    <div>
      <div>Anfragen: {{ store.counter }} </div>
   <div>
    <q-form @submit="queryChatBot(input_text)">
    <q-input label="Frage" input-class="text-center" v-model="input_text" :disable="status_query">
      <template v-slot:append>
        <q-icon name="search" class="cursor-pointer" @click="queryChatBot(input_text)"/>
      </template>
    </q-input>
  </q-form>
   </div>
   <div class="text-center" v-if="status_query">
        <q-spinner-bars
          color="primary"
          size="2em"
        />
        <q-tooltip :offset="[0, 8]">Warte auf Antwort ...</q-tooltip>
      </div>
      <div class="q-ma-xl my-box">
      {{  last_answer }}
    </div>
    </div>

  </q-page>
</template>

<script>

import { defineComponent, ref } from 'vue'
import { useCounterStore } from 'src/stores/queryAPI'
import { useQuasar } from 'quasar'

export default defineComponent({
  name: 'IndexPage',
  setup () {
    const $q = useQuasar()
    const store = useCounterStore()
    const status_query = ref(false)
    const last_answer = ref('')
    return {
      store, status_query, last_answer, 
      input_text: ref(''),

      queryChatBot: (payload) => {
        status_query.value = true        
        store.increment()
        store.query({message: payload})
        .then(res => {
          last_answer.value = res
        }).catch(err => {
          $q.notify({
            color: 'negative',
            position: 'top',
            message: 'Fehler: ' + err,
            icon: 'report_problem'
          })
        })
        .finally(() => {
          status_query.value = false
        })
      }
    }
  }
})
</script>
