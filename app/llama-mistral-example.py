from llama_cpp import Llama

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = Llama(
  model_path="./llm_models/capybarahermes-2.5-mistral-7b.Q4_K_M.gguf",  # Download the model file first
  n_ctx=8192,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=2,            # The number of CPU threads to use, tailor to your system and the resulting performance
  gpu_layers=0,           # The number of layers to offload to GPU, set to 0 if no GPU acceleration is available
  Verbose=True,           # Set to True to enable debug logging
  Seed=42,                 # Set to a non-zero value to seed the random number generator
)

system = """
Follow the instructions below to complete the task.
"""

user = """
Create a PHP script to scan a directory and print the contents of the directory.
"""

message = f"<s>[INST] {system} [/INST]</s>{user}"
output = llm(message, echo=True, stream=False, max_tokens=4096)
print(output['usage'])
output = output['choices'][0]['text'].replace(message, '')
print(output)