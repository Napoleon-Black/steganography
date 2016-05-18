# -*- coding: utf8 -*-

import pyexiv2
import random
import string

from itertools import product
from PIL import Image


class UnhideMessage(object):
       
    def unhide_message(self, imagefile, image_type):

        # Unhide file from PNG/BMP image
        if image_type[0].lower() == '.png' or image_type[0].lower() == '.bmp':
            image = Image.open(imagefile)
            pix = image.load()
            sizex, sizey = image.size
            nextindex = product(range(sizex), range(sizey))

            # find length of name
            name_len = 0
            for i in range(7, -1, -1):
                index = next(nextindex)
                b = pix[index][2]
                lastbit = bin(b)[-1:]
                if lastbit == '1':
                    name_len += 2 ** i

            # find name
            name = []
            for i in range(name_len):
                part = 0
                for i in range(7, -1, -1):
                    index = next(nextindex)
                    b = pix[index][2]
                    lastbit = bin(b)[-1:]
                    if lastbit == '1':
                        part += 2 ** i
                name.append(chr(part))

            # find length of message
            message_len = 0
            for i in range(7, -1, -1):
                index = next(nextindex)
                b = pix[index][2]
                lastbit = bin(b)[-1:]
                if lastbit == '1':
                    message_len += 2 ** i

            # find message
            message = []
            for i in range(message_len):
                part = 0
                for i in range(7, -1, -1):
                    index = next(nextindex)
                    b = pix[index][2]
                    lastbit = bin(b)[-1:]
                    if lastbit == '1':
                        part += 2 ** i
                message.append(chr(part))

            if name == []:
                name = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(500))
            else:
                name = ''.join(name)

            if message == []:
                message = ''.join(
                    random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(500))
            else:
                message = ''.join(message)

            return name, message

        # Unhide file from JPG/JPEG image
        elif image_type[0].lower() == '.jpg' or '.jpeg':

            metadata = pyexiv2.ImageMetadata(imagefile)
            metadata.read()
            tag = metadata['Exif.Photo.UserComment']
            secret_message = tag.value.encode('utf-8')
            separate_message = secret_message.split('OO')

            fix = {'name': [], 'message': []}

            uni_name = separate_message[0].split('O')
            for part in uni_name:
                fix['name'].append(chr(int(part)))
            fix['name'] = ''.join(fix['name'])

            uni_message = separate_message[1].split('O')
            for part in uni_message:
                fix['message'].append(chr(int(part)))
            fix['message'] = ''.join(fix['message'])

            return fix['name'], fix['message']



