from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import os


# Load the .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")
#print(openai.api_key)  # Debug: Print to ensure the API key is loaded



# Initialize Flask app
app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Get user input from the request
        data = request.json
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        client = openai.Client()
        q=client.chat.completions.create(
            model="gpt-4o", 
            messages=[{"role":"user",  "content":"WAZZUP!"}]
        )

        # Get the response from OpenAI
        response_content = q.choices[0].message.content
        return jsonify({"response": response_content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
