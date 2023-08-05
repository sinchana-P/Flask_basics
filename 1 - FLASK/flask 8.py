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

# SQLAlchemy because:
# it makes way easier to save information, because we can write all our database stuff, in PYTHON code rather than writing SQL queries.

# columns: (gonna represent) pieces of information
# rows: (gonna represent) individual items

# here, we wanna store users
# user : object

# define "class" which is gonna represent this user "object" in our db
# db.Model: as the inheritance, which means it is database Model, which has a few methods & things, that r inherited from it.
# properties: (write them as) class attributes

# users: below is a "MODEL"

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

# name = db.Column("name", db.String(100))
# email = db.Column("email", db.String(100))

# "name" , "email" : what gonna happen if I don't use these is: it will just use the variable name, which is fine.
# __init__ () :this method gonna take variables that we need to create a new object because, technically we can store some values here, that are gonna be none values (or) no values
# e.g Gender: Male, Female, No value
# _id: created automatically


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

        found_user = users.query.filter_by(name = user).first()     # ig, it selects complete row (Object)
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

        # This is for "POST" request of EMAIL
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email

            # instead of just saving in the session, save changes in db
            found_user = users.query.filter_by(name = user).first() 
            found_user.email = email
            db.session.commit() 

            flash("Email was saved!")

        # This is for "GET" request of EMAIL
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


# note:
# upto now, we r just saving user,email data in only SESSIONS.
# i.e :
# 1. Saving new data to Session.
# 2. Retrieving old data from Session.

# ---------------SQLAlchemy INSTALL-----------------

# SQLAlchemy Database:
# Databases & how we can actually save user specific information.


# To Install:
# pip install flask-sqlalchemy

# ----------------------db------------------------


# db.create_all() : create the database, if it doesn't already exist in our program, whenever we run this application
