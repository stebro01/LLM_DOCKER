from llama_cpp import Llama

class LlamaModelLoader:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = Llama(model_path=self.model_path)
    
    def generate_response(self, system_message, user_message, max_tokens=100):
        prompt = f"""<s>[INST] <<SYS>>
{system_message}
<</SYS>>
{user_message} [/INST]"""
        
        return self.model(prompt, max_tokens=max_tokens, echo=True)
