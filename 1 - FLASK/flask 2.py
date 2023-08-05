# 2. templates

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html") 
    
@app.route("/<name>")
def home(name):
    # return render_template("index.html", content = name, r = 2) 
    
    # to pass list from backend, and to pass this to display in frontend.
    return render_template("index.html", content = ["tim", "joe", "bill"], r = 2) 

if __name__ == "__main__":
    app.debug = True
    app.run()




# to pass information from this "backEnd" Flask to "frontEnd" index.html
