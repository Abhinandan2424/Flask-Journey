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




if __name__ == "__main__":
    app.run(debug=True)