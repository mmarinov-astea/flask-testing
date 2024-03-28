from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Martin"

if __name__ == "__main__":
    print("It works!")
    app.run(debug=False)