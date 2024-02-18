# LLM DOCKER

I want to create a docker container to run LLM.

<!-- important note -->
## Important Note

The LLM models are designed to work on the CPU. 

They need to be downloaded separately and placed in the `llm_models` folder.

## Resources

- https://medium.com/@penkow/how-to-run-llama-2-locally-on-cpu-docker-image-731eae6398d1

- https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main

## Access

- start the docker and enter it

### Execute the python script

```bash
python src/llama_cpu.py
```

### Acess the API

```bash
curl -X POST -H "Content-Type: application/json" -d '{ 
  "system_message": "You are a helpful assistant",
  "user_message": "Generate a list of 5 funny dog names",
  "max_tokens": 100
}' http://127.0.0.1:5001/llama
```