from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def student ():
    return render_template(
        "Student_profile.html",
        name = "Abhinandan",
        is_Topper = True,
        Subjects = ["Maths", "Science", "Python"]
    )



if __name__ == "__main__":
    app.run(debug=True)