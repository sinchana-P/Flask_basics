from flask import Blueprint, render_template

# ("second", __name__, ) : "second": name of the blueprint, __name__: represents name of this file, special python variable,
# optional parameters: static_folder, template_folder.
second = Blueprint("second", __name__, static_folder="static", template_folder="templates")

@second.route("/home")
@second.route("/")
def home():
    return render_template("home.html") 

@second.route("/test")
def test():
    return "<h1>Test Page</h1>"

 
 