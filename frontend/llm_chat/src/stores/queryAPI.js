import { defineStore } from 'pinia';
import axios from 'axios';

export const useCounterStore = defineStore('counter', {
  state: () => ({
    counter: 0
  }),

  getters: {
    doubleCount (state) {
      return state.counter * 2
    }
  },

  actions: {
    increment () {
      this.counter++
    },

    async query(payload) {
      console.log('query', payload)

      let data = JSON.stringify({
        "system_message": "You are a helpful assistant",
        "user_message": payload.message,
        "max_tokens": 100
      });

      let config = {
        method: 'post',
        maxBodyLength: Infinity,
        url: 'http://localhost:5001/llama',
        headers: { 
          'Content-Type': 'application/json'
        },
        data : data
      };
      return new Promise((resolve, reject) => {
        axios(config).then(response => {
          console.log('response', response)
          const txt = response.data.choices[0].text
          const splitTxt = txt.split('[/INST]');
          const restOfTxt = splitTxt[1];
          resolve(restOfTxt)
        }).catch(error => {
          console.log('error', error)
          reject(error)
        })
      })
    }
  }
})
