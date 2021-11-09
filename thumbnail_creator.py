# Creates thumbnails from images in a folder.
# Will Skip non-images and unsupported formats.
import os
from os.path import isfile, join
from PIL import Image
import logging

images_path = "/Images/"
thumbnails_path = "/Images/Thumbnails/"
thumbnail_size = [400, 400]
not_thumbnailed = []

files = [f for f in os.listdir(images_path) if isfile(join(images_path, f))]
for file in files:
    try:
        image = Image.open( images_path + file)
        image.thumbnail(thumbnail_size)
        image.save(thumbnails_path + file)
    except IOError:
        not_thumbnailed.append(file)
        logging.warning("Image cannot be thumbnailed", exc_info=True)
print(not_thumbnailed)