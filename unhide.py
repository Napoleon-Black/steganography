# -*- coding: utf8 -*-

import exiftool
import random, string
from itertools import product
from PIL import Image


class UnhideMessage(object):

    if image_type == '.jpg' or image_type == '.jpeg':
        # Unhide file from JPG/JPEG image
        def unhide_message(imagefile):
            with exiftool.ExifTool() as et:
                message = et.get_tag_batch('Comment', [imagefile])
            return message
    else:
        # Unhide file from PNG/BMP image
        def unhide_message(self, imagefile):
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
