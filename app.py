from flask import Flask, render_template, Response
from detect import counting_cars
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/technology')
def technology():
    return render_template('technology.html')


@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    return Response(counting_cars(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)