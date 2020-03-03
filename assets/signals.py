# This code is required to ensure imported photos are stored in the proper
# rotation.  A receiver decorator has been placed in assets/models.py to
# receive a signal and execute this code whenever the a photo is saved 
# within the database.

from PIL import Image, ExifTags
def rotate_image(filepath):
  try:
    print('Current filepath in rotate_image = %s' % filepath)
    image = Image.open(filepath)
    for orientation in ExifTags.TAGS.keys():
      if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = dict(image._getexif().items())

    if exif[orientation] == 3:
        image = image.rotate(180, expand=True)
    elif exif[orientation] == 6:
        image = image.rotate(270, expand=True)
    elif exif[orientation] == 8:
        image = image.rotate(90, expand=True)
    image.save(filepath)
    image.close()
  except (AttributeError, KeyError, IndexError):
    # cases: image don't have getexif
    pass