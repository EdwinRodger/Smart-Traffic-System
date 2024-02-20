from flask import Flask, render_template, Response
from vehicle import counting_cars
# from detect import counting_cars

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("home.html")


@app.route("/technology")
def technology():
    return render_template("technology.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/sign-up")
def signup():
    return render_template("signup.html")


@app.route("/demo")
def demo():
    return render_template("demo.html")


@app.route("/video_feed")
def video_feed():
    return Response(
        counting_cars(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True)
