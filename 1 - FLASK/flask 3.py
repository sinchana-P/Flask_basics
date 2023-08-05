# 3. Adding Bootstrap & Template Inheritance.

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
    
@app.route("/")
def home():
        return render_template("index.html") 

    
@app.route("/test")
def test():
        return render_template("new.html") 


if __name__ == "__main__":
    # app.debug = True
    app.run(debug=True)



# Template Inheritance :
# allows u not to repeat the HTML code or JAVASCRIPT throughout ur entire website

# (debug=True) : Allows us to not to re-run the server, every time u make a change, bcz it will be autmatically detecting those changes & updating the website for us.
