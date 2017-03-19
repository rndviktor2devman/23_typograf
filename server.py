from flask import Flask, render_template, request
from nice_format import text_format

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html', text=('', ''))


@app.route('/', methods=['POST'])
def nice_format():
    input_text = request.form['text']
    result = text_format(input_text)
    return render_template('form.html', text=(input_text, result))

if __name__ == "__main__":
    app.run()
