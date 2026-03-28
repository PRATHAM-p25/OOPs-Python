from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add")
def add_feedback():
    return render_template("add.html")

@app.route("/list")
def list_feedback():
    return render_template("list.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)