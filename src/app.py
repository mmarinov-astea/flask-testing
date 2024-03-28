import os

from flask import Flask

app = Flask(__name__)

database_url = os.environ["DATABASE_URL"]
print("Using database: {}".format(database_url))

@app.route('/')
def hello():
    return "Hello, {}".format(database_url)

if __name__ == "__main__":
    print("It works!")
    app.run(debug=False)