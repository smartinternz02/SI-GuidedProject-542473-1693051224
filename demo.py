from flask import Flask

app = Flask(__name__)
@app.route("/")
def hi():
    return "Welcome all"
@app.route("/type/<desg>")
def desg(desg):
    return " Welcome all hi " +desg+"to class"

if __name__ == "__main__":
    app.run(debug=True)