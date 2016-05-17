# -*- coding: utf8 -*-

import pyexiv2
import random, string
from itertools import product
from PIL import Image


class UnhideMessage(object):
       
    def unhide_message(self, imagefile, image_type):

        # Unhide file from PNG/BMP image
        if image_type[0].lower() == '.png':
            image = Image.open(imagefile)
            pix = image.load()
            sizex, sizey = image.size
            nextindex = product(range(sizex), range(sizey))

            # find length
            messagelen = 0
            for i in range(7,-1,-1):
                index = next(nextindex)
                b = pix[index][2]
                lastbit = bin(b)[-1:]
                if lastbit=='1':
                    messagelen += 2**i

            message = []
            for i in range(messagelen):
                part = 0
                for i in range(7,-1,-1):
                    index = next(nextindex)
                    b = pix[index][2]
                    lastbit = bin(b)[-1:]
                    if lastbit=='1':
                        part += 2**i
                message.append(chr(part))
            if message == []:
                return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(500))
            else:
                return ''.join(message)

        # Unhide file from JPG/JPEG image
        elif image_type[0].lower() == '.jpg' or '.jpeg':

            metadata = pyexiv2.ImageMetadata(imagefile)
            metadata.read()
            tag = metadata['Exif.Photo.UserComment']
            fix_message = tag.value.encode('utf-8')
            separate_message = fix_message.split('O')

            message = []
            for part in separate_message:
                message.append(chr(int(part)))
            message = ''.join(message)

            print message
            return message

