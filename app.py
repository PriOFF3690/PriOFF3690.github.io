from flask import Flask

SERVER = Flask("__main__")
HOST = "localhost"
PORT = 8081

@SERVER.route("/")
def index():
    return "Welcome to the portfolio"

SERVER.run(
    host=HOST,
    port=PORT,
    debug=True
)