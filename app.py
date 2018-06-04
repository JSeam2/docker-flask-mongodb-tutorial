from flask import Flask

app = Flask("DockerTutorial")

@app.route("/")
def index():
    return "Hello"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

