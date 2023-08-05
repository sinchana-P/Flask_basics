# 5. SESSIONS :

from flask import Flask, redirect, url_for, render_template, request, session
# to set up the max time -- the session could last for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"  
app.permanent_session_lifetime = timedelta(days=5)

@app.route("/")
def home():
        return render_template("index.html") 


@app.route("/login", methods=["POST", "GET"])
# whether we called GET request or POST request
def login():
    if request.method == "POST":
        
        # to make the session permanent
        session.permanent = True
        user = request.form['nm']

        # to set up data for our session
        session["user"] = user                                                      
 
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
      user = session["user"]
      return f"<h1> Hello {user}! </h1>"
    else:
        return redirect(url_for("login"))
    

@app.route("/logout")    
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)


# Sessions:
# They r temporary.
# They r stored on the Server.
# They r not stored on the client side.
# They r kind of just designed for just quick information and a way to pass stuff around our server.

# TypeError: user() missing 1 required positional argument: 'user'

