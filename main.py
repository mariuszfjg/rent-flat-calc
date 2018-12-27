from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello World!</h1><br>from <h3><b>RPI</b></h3>"


if __name__ == "__main__":
    app.run()
