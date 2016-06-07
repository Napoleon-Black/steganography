# -*- coding: utf8 -*-

import pyexiv2

from itertools import product
from PIL import Image


class HideMessage(object):
    """HideMessage class takes image and text files then transform 
    information about hiden file and it's content in specific way 
    to a string of code. Next insernt that string of code into new 
    image file with the name you want."""

    # Transform text file name and content into binary code
    def bin_message(self, message, file_name):

        bin_message = [] # List of total hiden info (file name and content) in binary code
        name_len = len(file_name)
        bin_name_len = bin(name_len)[2:]
        if len(bin_name_len) < 8:
            bin_name_len = '0' * (8 - len(bin_name_len)) + bin_name_len
        bin_message.append(bin_name_len)

        for char in file_name:
            part = ''.join(format(ord(part), 'b') for part in char)
            partlen = len(part)
            if (partlen < 8):
                part = '0' * (8 - partlen) + part
            bin_message.append(part)

        message_len = len(message)
        bin_message_len = bin(message_len)[2:]
        if len(bin_message_len) < 15:
            bin_message_len = '0' * (15 - len(bin_message_len)) + bin_message_len
        bin_message.append(bin_message_len)

        for char in message:
            part = ''.join(format(ord(part), 'b') for part in char)
            partlen = len(part)
            if (partlen < 8):
                part = '0' * (8 - partlen) + part
            bin_message.append(part)

        return ''.join(bin_message) # Return string of total hiden information

    # Insert information into image file
    def hide_message(self, message, imagefile, outfile, image_type, file_name):

        bin_message = self.bin_message(message, file_name)
        image = Image.open(imagefile)

        # Check needed hiding method
        if image_type[0].lower() == '.png' or image_type[0].lower() == '.bmp':
            pix = image.load()
            sizex, sizey = image.size
            nextindex = product(range(sizex), range(sizey))

            for char in bin_message:
                index = next(nextindex)
                pix_index = list(pix[index])
                blue = pix_index[2]
                lastbit = bin(blue)[-1:]

                if char == '0':
                    if lastbit == '1':
                        blue -= 1
                elif char == '1':
                    if lastbit == '0':
                        blue += 1

                pix_index[2] = blue # Modify pixel's blue point
                pix[index] = tuple(pix_index)

            image.save(outfile)

        elif image_type[0].lower() == '.jpg' or '.jpeg':
            image.save(outfile, quality=100)
            fix = {'name': [], 'message': []}

            # Transform text file name and content into unicode
            for char in file_name:
                part = ord(char)
                fix['name'].append(str(part))
            fix['name'] = 'O'.join(fix['name'])

            for char in message:
                part = ord(char)
                fix['message'].append(str(part))
            fix['message'] = 'O'.join(fix['message'])
            # Unite file name and content into single string
            secret_message = fix['name'] + 'OO' + fix['message']

            metadata = pyexiv2.ImageMetadata(outfile)
            metadata.read()

            key = 'Exif.Photo.UserComment'
            value = secret_message
            metadata[key] = pyexiv2.ExifTag(key, value)

            metadata.write()





