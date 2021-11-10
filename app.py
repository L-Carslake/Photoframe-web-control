from flask import Flask, request, render_template, send_from_directory
import os
from os.path import isfile, join
from pykeyboard import PyKeyboard
import time
import configparser

os.system("export DISPLAY=:0")
keyboard = PyKeyboard()
app = Flask(__name__)

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'images_directory': './Images',
    'thumbnails_directory': './Images/Thumbnails',
    'host_ip': '192.168.0.98',
    'name': 'Test Photoframe',
    'unique_id': 'b8507fe7-dc48-40df-8ef4-4d0fffccdc05'
}
config.read('config.ini')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('next'):
            next_image()
        if request.form.get('prev'):
            previous_image()
        if request.form.get('refresh_image'):
            update_current_image_file()
    time.sleep(0.4)  # Waits for image to be reloaded
    return render_template("index.html", current_image_name=get_current_image_name())


# Custom static data
@app.route('/current_image')
def current_image():
    return send_from_directory(config['DEFAULT']['images_directory'], get_current_image_name())


# Custom static data
@app.route('/cdn/<path:filename>')
def custom_static(filename):
    return send_from_directory(config['DEFAULT']['images_directory'], filename)


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
    if command in ["play", "pause", "toggle", "stop", "volume", "playplaylist", "repeat", "random", "clearQueue",
                   "playplaylist"]:
        # Unimplemented commands
        print('Unimplemented command called')
        return "", 404
    return "", 404


@app.route('/api/v1/getState/')
def getstate():
    update_current_image_file()
    time.sleep(0.4)  # Waits for image to be reloaded
    state = {"status": "play",
             "position": 2,
             "title": "Test Frame",
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
    info = {"id": config['DEFAULT']['unique_id'],
            "host": config['DEFAULT']['host_ip'],
            "name": config['DEFAULT']['name'],
            "type": "device",
            "serviceName": "Volumio",
            "systemversion": "2.803",
            "builddate": "Tue Jul 28 21:28:37 CEST 2020",
            "variant": "media",
            "hardware": "Photoframe"
            }
    return info


@app.route('/api/v1/getSystemVersion/')
def getSystemVersion():
    version = {"systemversion": "2.632",
               "builddate": "Thu Oct  3 21:47:57 CEST 2019",
               "variant": "media",
               "hardware": "Photoframe"}
    return version


@app.route('/api/v1/listplaylists/')
def list_playlists():
    return {}


@app.route('/api/v1/browse/')
def browse():
    if "uri" not in request.args:
        top_level_navigation = {
            "navigation": {
                "lists": [
                    {
                        "albumart": "",
                        "name": "Images",
                        "uri": "Images",
                        "plugin_type": "music_service",
                        "plugin_name": "mpd"
                    }
                ]
            }
        }
        return top_level_navigation
    else:
        media_list = list_images()
        return media_list


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
    path = open(config['DEFAULT']['images_directory'] + "/currentImage.txt", "r").read().strip()
    split_path = path.split("/")
    print(split_path[2])
    return split_path[2]


def list_images():
    file_names = [f for f in os.listdir(config['DEFAULT']['images_directory'])
                  if isfile(join(config['DEFAULT']['images_directory'], f))]
    structured_files = []
    for file in file_names:
        structured_files.append({
            "service": "mpd",
            "type": "song",
            "title": file,
            "artist": "",
            "album": "Images",
            "uri": "/cdn/" + file,
            "albumart": "/cdn/Thumbnails/" + file
        }
        )
    media_list = {
        "navigation": {
            "prev": {
                "uri": "music-library"
            },
            "lists": [
                {
                    "availableListViews": [
                        "grid",
                        "list"
                    ],
                    "items": structured_files
                }
            ]
        }
    }
    return media_list
