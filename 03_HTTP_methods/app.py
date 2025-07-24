from flask import Flask ,request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hey Abhi! this new Flask Application"

@app.route('/about')
def about():
    return "This is about us!"

@app.route("/contact")
def contact():
    return "This is contact page!"

@app.route("/submit", methods =['GET','POST'])
def submit():
    if request.method == 'POST':
        return 'You send data'
    else:
        return 'You are only viewing the form'


if __name__ == "__main__":
    app.run(debug=True)