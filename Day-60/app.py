from flask import Flask, render_template, abort
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

class ValidationError(Exception):
    def __init__(self, message="Validation failed"):
        self.message = message

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/error-demo")
def error_demo():
    return render_template("error_demo.html")

@app.route("/trigger-404")
def trigger_404():
    abort(404)

@app.route("/trigger-500")
def trigger_500():
    raise RuntimeError("Server error")

@app.route("/trigger-custom")
def trigger_custom():
    raise ValidationError("Invalid input: demo custom exception")

@app.errorhandler(404)
def handle_404(e):
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template("errors/500.html"), 500

@app.errorhandler(ValidationError)
def handle_custom(e):
    return render_template("errors/custom.html", error=e), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)