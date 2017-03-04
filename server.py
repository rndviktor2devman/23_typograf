from flask import Flask, render_template, request
from nice_format import text_format

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/format', methods=['POST'])
def nice_format():
    text = text_format(request.form['text'])
    return text

if __name__ == "__main__":
    app.run()
