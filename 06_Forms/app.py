from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "Abhi" and password =="123":
        return render_template("welcome.html", name = "username")
    
    else:
        return "Invalid credentials"
    
# @app.route("/logout")
# def logout():
#     return render_template("login.html")
    

if __name__ == "__main__":
    app.run(debug=True)