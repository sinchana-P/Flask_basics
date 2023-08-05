from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the main page <h1> HELLO </h1>" 
    
@app.route("/<name>")    
def user(name): 
    return f"Hello {name}!" 

@app.route("/admin")
def admin():
    return redirect(url_for("home"))  

if __name__ == "__main__":
    app.run()


# run: python3 'tutorial 1.py' 

# -----------------------------------------------------------------------------------------------------------------------


# from flask import Flask, redirect, url_for

# app = Flask(__name__)

# # last step, to define how we can access this specific page     
# # @app.route("/")                                               
                                                                
# # define the pages that will be on our website                  
# # def home():                                                   
#     # return " Hello! this is the main page <h1> HELLO </h1> "  

# @app.route("/")
# def home():
#     return "Hello! this is the main page <h1> HELLO </h1>" 
    
# # whatever we pass in <> angular brackets, it gonna be sent as parameter for function (user)  
# @app.route("/<name>")    
# def user(name): 
#     return "Hello {name}!" 
# # f: to do parsing 

# @app.route("/admin")
# def admin():
#     return redirect(url_for("home")) 
# # put the name of the function (home) that we're going to be redirecting to, rather than just putting "/". 


# if __name__ == "__main__":
#     app.run()


# # run: python3 'tutorial 1.py'


