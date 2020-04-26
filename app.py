from flask import Flask, request, render_template, send_from_directory
import os
from pykeyboard import PyKeyboard
import time

os.system("export DISPLAY=:0")
keyboard = PyKeyboard()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('next'):
            next_image()
        if request.form.get('prev'):
            previous_image()
    time.sleep(0.4) # Waits for image to be reloaded
    return render_template("index.html", current_image_name=get_current_image_name())


# Custom static data
@app.route('/current_image')
def current_image():
    return send_from_directory('/Images', get_current_image_name())


# Custom static data
@app.route('/cdn/<path:filename>')
def custom_static(filename):
    #TODO: Make path safe
    return send_from_directory('/Images', filename)


def next_image():
    # Next image
    keyboard.tap_key(keyboard.right_key)
    # Update Current image file
    update_current_image_file()
    return 0


def previous_image():
    # Previous image
    keyboard.tap_key(keyboard.left_key)
    # Update current image file
    update_current_image_file()
    return 0


def update_current_image_file():
    keyboard.type_string('0')
    return 0


def get_current_image_name():
    # Update the "/Images/currentImage.txt" file and read
    # Out: Path and file name of current photo (string)
    update_current_image_file()
    path = open("/Images/currentImage.txt", "r").read().strip()
    split_path = path.split("/")
    print(split_path[2])
    return split_path[2]

