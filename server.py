from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"


@app.route("/<name>/")
def dojo(name):
    return f"{name}"

@app.route('/say/flask')
def hello_flask():
    return "Hi Flask"


@app.route('/say/michael')
def hello_michaek():
    return "Hi Michael"


@app.route('/say/john')
def hello_john():
    return "Hi John"

@app.route('/repeat/<int:times>/<string:word>')
def repeater(times, word):
    collection = ''
    for index in range(times):
        collection += f"<p>{word}</p>"

    return collection

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."

if __name__== "__main__" :
    app.run(debug=True)