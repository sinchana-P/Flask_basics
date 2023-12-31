# 7. Using SQLAlchemy Database (half continued...)
# 8. Adding, Deleting & Updating Users w/ SQLAlchemy

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)
# set up few configuration properties
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# we're not tracking all the modifications to the database.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# db object
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all()) 


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['nm']
        session["user"] = user

        found_user = users.query.filter_by(name = user).delete()  

        for user in found_user:
            user.delete()                                                                                 
            
        if found_user:
            # check, if user Already exists
            session["email"] = found_user.email
            
        else:
            # else: if user doesn't exists
            usr = users(user, "")
            db.session.add(usr)         # Staging Area (not technically though), (can roll back to changes)
            db.session.commit() 

        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        else:
            return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email

            found_user = users.query.filter_by(name = user).first() 
            found_user.email = email
            db.session.commit() 

            flash("Email was saved!")

        else:
            if "email" in session:
                email = session["email"]

        return render_template("user2.html", email=email)

    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

   
@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(debug=True)

