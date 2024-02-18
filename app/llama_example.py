from llama_model_loader import LlamaModelLoader

# Path to your GGUF model
model_path = "./llm_models/llama-2-7b-chat.Q2_K.gguf"

# Create an instance of LlamaModelLoader
llama_loader = LlamaModelLoader(model_path=model_path)

# Define your system message and user message
system_message = "You are a helpful assistant"
user_message = "Generate a list of 5 funny dog names"

# Generate the response
response = llama_loader.generate_response(system_message, user_message, max_tokens=100)

# Print the response
print(response)