# app.py
from flask import Flask, render_template, request
from model import correct_spelling  # Importing the function from model.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spellcheck', methods=['POST'])
def spellcheck():
    text = request.form.get('text_input')
    corrected_text = correct_spelling(text)  # Using the imported function
    return render_template('index.html', original_text=text, corrected_text=corrected_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)