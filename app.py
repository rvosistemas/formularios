import os
from flask import render_template, request, redirect, url_for, Response
# from werkzeug.security import generate_password_hash, check_password_hash
from config import app, db
from Models.fields import Fields
from Models.logs import Logs


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        city = request.form['city']
        newField = Fields(
            full_name=full_name,
            email=email,
            city=city)
        db.session.add(newField)
        db.session.commit()

        q = db.session.query(Fields).filter_by(id=newField.id).first()
        newLog = Logs(field_id=q.id)

        db.session.add(newLog)
        db.session.commit()

        return redirect(url_for('view'))
    return render_template("form.html")


@app.route("/view")
def view():
    fields = db.session.query(Fields).all()
    return render_template("view.html", fields=fields)


@app.route("/file")
def file():
    logs = db.session.query(Logs).all()
    file = open(os.path.abspath(os.getcwd())+"/logs.txt", "w")
    for log in logs:
        q = db.session.query(Fields).filter_by(id=log.id).first()
        file.write(f" - {log} --> {q.full_name}" + os.linesep)
    file.close()
    return render_template("index.html")


if __name__ == "__main__":
    db.init_app(app)
    db.create_all()
    db.session.commit()

    app.run(debug=True)

# @app.route("/search")
# def search():
#     nickname = request.args.get("nickname")
#     user = Users.query.filter_by(username=nickname).first()
#     if user:
#         return user.username
#     return "the user doesn't exist"


# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         hashed_pw = generate_password_hash(
#             request.form["password"], method="sha256")
#         new_user = Users(username=request.form["username"], password=hashed_pw)
#         db.session.add(new_user)
#         db.session.commit()
#         return "You've registered successfully"
#     return render_template('signup.html')


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         user = Users.query.filter_by(username=request.form["username"]).first()
#         if user and check_password_hash(user.password, request.form["password"]):
#             return "You are logged in"
#         return "Your credentials are invalid, check and try again"
#     return render_template("login.html")
