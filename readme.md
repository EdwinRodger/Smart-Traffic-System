# Smart Traffic Detector

Smart Traffic Detector is used to detect the density of traffic and allows us to optimise traffic better using cameras and vehicle detection systems using AIML

### 1. Web Pages:

- The website has several routes defined using Flask's @app.route decorator, such as "/" for the homepage, "/technology" for the technology page, "/about" for the about page, etc.
- The render_template function is used to render HTML templates for these routes.

### 2. Authentication System:

- The website uses Flask and Flask-Login for authentication. Flask-Login is an extension for managing user sessions.
- There is a User class that extends flask_login.UserMixin, which helps in managing user sessions.
- Users and their passwords are stored in a mock database (users dictionary).
- The signup route handles both GET and POST requests. For a GET request, it renders the signup page, and for a POST request, it checks the provided username and password, logs in the user using Flask-Login if the credentials are valid, and redirects to the demo page.

### 3. Demo Page:

- The /demo route is protected using @flask_login.login_required, ensuring that only authenticated users can access the demo page.
- The demo route renders the "demo.html" template, which can display the processed video stream.

### 4. Video Processing:

- The /video_feed route is used for streaming video content. It utilizes the counting_cars generator function defined in the vehicle.py file.
- The counting_cars function reads frames from a video file (static\\videoTrim.mp4), performs background subtraction, contour detection, and object tracking to count the number of vehicles passing a specified line.
- The processed video frames are encoded as JPEG images and sent as a multipart response to the client using Flask's Response class. This allows for real-time streaming of the processed video.
- For prototype purposes, a weak vehicle detection system is used which can be updated to more enhanced detection system

### 5. Logout:

- The /logout route logs out the current user using flask_login.logout_user() and redirects to the homepage.


# To use the website:

Users can sign up using the "/sign-up" route, providing a username and password.
After signing up, users can log in, and authenticated users can access the demo page to view the processed video stream.


# How to run (currently works on windows)

1. Download code
2. Run `run.cmd`
   1. It will create virtual environment
   2. Install flask, numpy and opencv-python
   3. Run `127.0.0.1:5000` on default browser
   4. Run flask server

Alternatively you can follow below commands -

1. `pip install flask numpy opencv-contrib-python flask-login`
2. `flask run`
   
then open `127.0.0.1:5000` in your web browser to run the website