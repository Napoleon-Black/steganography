# -*- coding: utf8 -*-

import pyexiv2
import random
import string

from itertools import product
from PIL import Image


class UnhideMessage(object):
    """UnhideMessage class extracts hiden information from 
    given image file and tranform it to "normal" decimal 
    code string and return name and content of hiden text file"""

    def unhide_message(self, imagefile, image_type):


     # Extract information from PNG/BMP image
        if image_type[0].lower() == '.png' or image_type[0].lower() == '.bmp':
            image = Image.open(imagefile)
            pix = image.load()
            sizex, sizey = image.size
            nextindex = product(range(sizex), range(sizey))

            # Extract length of hiden file name
            name_len = 0
            for unit in range(7, -1, -1):
                index = next(nextindex)
                blue = pix[index][2] # Pixel's blue point
                lastbit = bin(blue)[-1:]
                if lastbit == '1':
                    name_len += 2 ** unit

            # Extract hiden file name
            name = []
            for char in range(name_len):
                part = 0
                for unite in range(7, -1, -1):
                    index = next(nextindex)
                    blue = pix[index][2] # Pixel's blue point
                    lastbit = bin(blue)[-1:]
                    if lastbit == '1':
                        part += 2 ** unite
                name.append(chr(part))

            # Extract length of hiden file content
            message_len = 0
            for unit in range(7, -1, -1):
                index = next(nextindex)
                blue = pix[index][2] # Pixel's blue point
                lastbit = bin(blue)[-1:]
                if lastbit == '1':
                    message_len += 2 ** unit

            # Extract hiden file content
            message = []
            for char in range(message_len):
                part = 0
                for unit in range(7, -1, -1):
                    index = next(nextindex)
                    blue = pix[index][2] # Pixel's blue point
                    lastbit = bin(blue)[-1:]
                    if lastbit == '1':
                        part += 2 ** unit
                message.append(chr(part))

            if name == []:
                name = ''.join(random.SystemRandom().choice(\
                    string.ascii_letters + string.digits) for _ in range(10))
            else:
                name = ''.join(name)

            if message == []:
                message = ''.join(
                    random.SystemRandom().choice(string.ascii_letters \
                                        + string.digits) for _ in range(500))
            else:
                message = ''.join(message)

            return name, message # Return name and content of hiden text file

        # Extract information from JPG/JPEG image
        elif image_type[0].lower() == '.jpg' or '.jpeg':

            fix = {'name': [], 'message': []}
            metadata = pyexiv2.ImageMetadata(imagefile)
            metadata.read()
            try:
                tag = metadata['Exif.Photo.UserComment']
                secret_message = tag.value.encode('utf-8')
                separate_message = secret_message.split('OO') # Separate hiden file name and content

                uni_name = separate_message[0].split('O') # Transform hiden file name to unicode
                for part in uni_name:
                    fix['name'].append(chr(int(part)))
                fix['name'] = ''.join(fix['name']) # Transform hiden file name to decimal code

                uni_message = separate_message[1].split('O') # Transform hiden file content to unicode
                for part in uni_message:
                    fix['message'].append(chr(int(part)))
                fix['message'] = ''.join(fix['message']) # Transform hiden file content to decimal code

            except KeyError:
                fix['name'] = ''.join(
                    random.SystemRandom().choice(string.ascii_letters \
                                    + string.digits) for _ in range(10))
                fix['message'] = ''.join(
                    random.SystemRandom().choice(string.ascii_letters \
                                    + string.digits) for _ in range(500))

            return fix['name'], fix['message'] # Return name and content of hiden text file



