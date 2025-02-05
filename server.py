from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import os
from flask_cors import CORS  # Import Flask-CORS

# Load the .env file
load_dotenv()

with open('preprompt.txt', 'r') as file:
    # Read the content of the file into a string
    preprompt = file.read()

# Retrieve the OpenAI API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Get user input from the request
        data = request.json
        user_message = data.get("message", "")
        print(type(user_message))

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        client = openai.Client()
        prompty = preprompt + user_message
        q = client.chat.completions.create(
            model="gpt-4o", 
            messages=[{"role": "user", "content": prompty}]
        )

        # Get the response from OpenAI
        response_content = q.choices[0].message.content
        return jsonify({"response": response_content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

