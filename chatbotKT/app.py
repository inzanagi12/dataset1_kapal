from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral:7b"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    payload = {
        "model": MODEL_NAME,
        "prompt": user_input,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=60)
        data = response.json()
        return jsonify({
            "response": data.get("response", "Sorry, I didn't understand that.")
        })
    except Exception as e:
        return jsonify({
            "response": f"Error: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)