@REM @echo off

@REM Step 1: Create a virtual environment
python -m venv myenv

@REM Step 2: Activate the virtual environment
call myenv\Scripts\activate

@REM Step 3: Install Flask, NumPy, and OpenCV-Python
pip install flask numpy opencv-python

@REM Step 4: Open 127.0.0.1:5000 in the default browser
start http://127.0.0.1:5000

@REM Step 5: Run Flask app
python app.py