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
        if request.form.get('refresh_image'):
            update_current_image_file()
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



# Below is API for homeassistant integration
@app.route('/api/v1/commands/')
def commands():
    command = request.args.get('cmd')
    if command == 'next':
        # Next
        next_image()
        print('Next')
        return ""
    if command == 'prev':
        # Previous
        previous_image()
        print('Previous')
        return ""
    if command  in ["play", "pause", "toggle", "stop", "volume", "playplaylist", "repeat", "random", "clearQueue", "playplaylist"]:
        # Unimplemented commands
        print('Unimplemented command called')
        return ""
    return "", 404

@app.route('/api/v1/getState/')
def getstate():
    update_current_image_file()
    time.sleep(0.4) # Waits for image to be reloaded
    state = {  "status": "play",
               "position": 2,
               "title": "Photoframe",
               "artist": get_current_image_name(),
               "album": "",
               "albumart": "/cdn/" + get_current_image_name(),
               "uri": "",
               "trackType": "",
               "seek": 53057,
               "duration": 809,
               "samplerate": "96 kHz",
               "bitdepth": "24 bit",
               "channels": 2,
               "random": False,
               "repeat": False,
               "repeatSingle": False,
               "consume": False,
               "volume": 43,
               "disableVolumeControl": False,
               "mute": False,
               "stream": "flac",
               "updatedb": False,
               "volatile": False,
               "service": "mpd"
             }
    return state

@app.route('/api/v1/getSystemInfo/')
def getSystemInfo():
    info = {  "id": "b8507fe7-dc48-40df-8ef4-4d0fff88dc05",
              "host": "http://192.168.0.49",
              "name": "Photoframe",
              "type": "device",
              "serviceName": "Volumio",
              "state": {
                "status": "play",
                "volume": 43,
                "mute": false,
                "artist": get_current_image_name(),
                "track": "Photoframe",
                "albumart": "/cdn/" + get_current_image_name()
              },
              "systemversion": "2.803",
              "builddate": "Tue Jul 28 21:28:37 CEST 2020",
              "variant": "volumio",
              "hardware": "pi"
             }
    return info


@app.route('/api/v1/listplaylists/')
def list_playlists():
    return {}


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

