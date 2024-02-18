from flask import Flask, request, jsonify
from llama_model_loader import LlamaModelLoader
from flask_cors import CORS


# Path to your GGUF model
model_path = "./llm_models/llama-2-7b-chat.Q2_K.gguf"
llama_loader = LlamaModelLoader(model_path=model_path)

# Create a Flask object
app = Flask("Llama server")
CORS(app)
model = None

@app.route('/llama', methods=['POST'])
def generate_response():
    global model
    
    try:
        data = request.get_json()

        # Check if the required fields are present in the JSON data
        if 'system_message' in data and 'user_message' in data and 'max_tokens' in data:
            system_message = data['system_message']
            user_message = data['user_message']
            max_tokens = int(data['max_tokens'])

            # Generate the response
            print('asking ai for response...')
            response = llama_loader.generate_response(system_message, user_message, max_tokens)
            print('response received')
            return jsonify(response)

        else:
            return jsonify({"error": "Missing required parameters"}), 400

    except Exception as e:
        return jsonify({"Error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)