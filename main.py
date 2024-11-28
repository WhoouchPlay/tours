from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tour/")
def tour():
    return render_template("tour.html")

@app.route("/departure/")
def departute():
    return render_template("departure.html")

if __name__ == "__main__":
    app.run(debug=True, port=5012)