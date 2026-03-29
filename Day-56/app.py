from flask import Flask, render_template, request

app = Flask(__name__)

def get_user_role():
    role = request.args.get("role", "user")
    if role not in ["user", "admin"]:
        return "user"
    return role

@app.route("/")
def home():
    return render_template("index.html", user_role=get_user_role())

@app.route("/courses")
def courses():
    course_list = ["Python", "SQL", "HTML"]
    return render_template("courses.html", user_role=get_user_role(), courses=course_list)

@app.route("/profile")
def profile():
    return render_template("profile.html", user_role=get_user_role())

@app.route("/admin")
def admin():
    return render_template("admin.html", user_role=get_user_role())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)