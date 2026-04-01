from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
import pymysql
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    return pymysql.connect(
        host=app.config["MYSQL_HOST"],
        user=app.config["MYSQL_USER"],
        password=app.config["MYSQL_PASSWORD"],
        database=app.config["MYSQL_DATABASE"],
        port=app.config["MYSQL_PORT"],
        cursorclass=pymysql.cursors.DictCursor
    )

def require_login(f):
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

def require_admin(f):
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        if session.get("role") != "admin":
            abort(404)
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@app.route("/")
@require_login
def home():
    return render_template("index.html")

@app.route("/thank-you")
@require_login
def thank_you():
    return render_template("thank_you.html")

@app.route("/submit", methods=["POST"])
@require_login
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

        flash("Feedback saved successfully", "success")

    except Exception:
        flash("Error saving feedback", "error")

    return redirect(url_for("thank_you"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin123":
            session["user_id"] = 1
            session["username"] = "admin"
            session["role"] = "admin"
            return redirect(url_for("dashboard"))

        elif username == "user" and password == "user123":
            session["user_id"] = 2
            session["username"] = "user"
            session["role"] = "user"
            return redirect(url_for("dashboard"))

        flash("Invalid credentials", "error")
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out", "success")
    return redirect(url_for("login"))

@app.route("/dashboard")
@require_login
def dashboard():
    return render_template("dashboard.html")

@app.route("/admin")
@require_admin
def admin():
    return render_template("admin.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("errors/404.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)