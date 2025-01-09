from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import os
from flask_cors import CORS  # Import Flask-CORS

# Load the .env file
load_dotenv()

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

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Send user_message to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace 'gpt-4o' with 'gpt-4' if necessary
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        # Get the response from OpenAI
        response_content = response.choices[0].message.content
        return jsonify({"response": response_content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
