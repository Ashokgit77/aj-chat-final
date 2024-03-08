import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Set up the model
genai.configure(api_key="AIzaSyCPLxIajqIGvDgas_7eANyVbdTcPfc87rs")
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
model = genai.GenerativeModel(model_name="gemini-1.0-pro",generation_config=generation_config, safety_settings=safety_settings)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    question = request.form['question']
    convo = model.start_chat(history=[
    ])
    convo.send_message(question)
    answer = convo.last.text
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)