from flask import Flask, request, render_template
import os
from pykeyboard import PyKeyboard

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
        return render_template("index.html")

    return render_template("index.html")


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

