# -*- coding: utf8 -*-

import pyexiv2

from itertools import product
from PIL import Image

class HideMessage(object):

    def bin_message(self, message, file_name):

        bin_message = []

        file_name = file_name[0: file_name.index('.')]
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
        if len(bin_message_len) < 8:
            bin_message_len = '0' * (8 - len(bin_message_len)) + bin_message_len

        bin_message.append(bin_message_len)

        for char in message:
            part = ''.join(format(ord(part), 'b') for part in char)
            partlen = len(part)
            if (partlen < 8):
                part = '0' * (8 - partlen) + part
            bin_message.append(part)
        return ''.join(bin_message)

    def hide_message(self, message, imagefile, outfile, image_type, file_name):

        binmessage = self.bin_message(message, file_name)
        image = Image.open(imagefile)

        if image_type[0].lower() == '.png' or image_type[0].lower() == '.bmp':
            pix = image.load()
            sizex, sizey = image.size
            nextindex = product(range(sizex), range(sizey))

            for m in binmessage:
                index = next(nextindex)
                pix_index = list(pix[index])
                b = pix_index[2]
                lastbit = bin(b)[-1:]
                if m == '0':
                    if lastbit == '1':
                        b -= 1
                elif m == '1':
                    if lastbit == '0':
                        b += 1

                pix_index[2] = b
                pix[index] = tuple(pix_index)

            image.save(outfile)

        elif image_type[0].lower() == '.jpg' or '.jpeg':
            image.save(outfile, quality=100)
            file_name = file_name[0: file_name.index('.')]

            fix = {'name': [], 'message': []}

            for char in file_name:
                part = ord(char)
                fix['name'].append(str(part))
            fix['name'] = 'O'.join(fix['name'])

            for char in message:
                part = ord(char)
                fix['message'].append(str(part))
            fix['message'] = 'O'.join(fix['message'])

            secret_message = fix['name'] + 'OO' + fix['message']

            metadata = pyexiv2.ImageMetadata(outfile)
            metadata.read()

            key = 'Exif.Photo.UserComment'
            value = secret_message
            metadata[key] = pyexiv2.ExifTag(key, value)

            metadata.write()





