# 10. BLUEPRINTS & USING MULTIPLE PYTHON FILES

from flask import Flask, render_template
from second import second

app = Flask(__name__)
# app.register_blueprint(second, url_prefix="")

# whenever, we register Blueprint, we look at this, url_prefix="" , which in this case is blank ---> which means any url we pass it to the Blueprint, we see if anything matches
# so in this case we type "/" , we go to this Blueprint, we see that "/" matches, so immediately we retur & render "home.html".
# If we "/", doesn't exist, it's directed to test(). 
 
app.register_blueprint(second, url_prefix="/admin")

@app.route("/")
def test():
    return "<h1>TEST IN MAIN PAGE</h1>"

if __name__ == "__main__":
    app.run(debug=True)



# BLUEPRINTS: are just extensions of our app