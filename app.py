from flask import Flask, render_template

from config import config



app = Flask(__name__)

@app.route("/index")
def weatherWidget():
    return render_template("index.html")

if __name__ == "__main__":
    host = config["network"]["host"]
    port = config["network"]["port"]
    app.run(host, port)
