from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def startup():
# declare a dictionary and store it in a variable
# i will be iterateing over this dictionary inside of my index.html
    Users = [
        {'first_name' : 'Michael', 'last_name' : 'choi'},
        {'first_name' : 'John', 'last_name' : 'supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('index.html', user = Users)

if __name__ == '__main__':
    app.run(debug = True)