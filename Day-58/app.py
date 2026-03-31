from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# DB connection (mockable)
def get_db_connection():
    return pymysql.connect(
        host=app.config["MYSQL_HOST"],
        user=app.config["MYSQL_USER"],
        password=app.config["MYSQL_PASSWORD"],
        database=app.config["MYSQL_DATABASE"],
        port=app.config["MYSQL_PORT"],
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill all fields", "error")
        return redirect(url_for("home"))

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message)
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Thank you! Your feedback has been saved.", "success")

    except Exception:
        flash("Error saving feedback", "error")

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)