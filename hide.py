# -*- coding: utf8 -*-

from PIL import Image
from itertools import product

class HideMessage(object):

    def bin_message(self, message):
        messagelen = len(message)
        binlen = bin(messagelen)[2:]
        if len(binlen) < 8:
            binlen = '0' * (8 - len(binlen)) + binlen
        
        binmessage = []
        binmessage.append(binlen)
        for x in message:
            part = ''.join(format(ord(part), 'b') for part in x)
            partlen = len(part)
            if (partlen < 8):
                part = '0' * (8 - partlen) + part
            binmessage.append(part)
        return ''.join(binmessage)

    def hide_message(self, message, imagefile, outfile):
        binmessage = self.bin_message(message)
        image = Image.open(imagefile)
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

        # if imagefile.endswith('.jpeg'):
        #     image.save(outfile, "jpeg")
        # elif imagefile.endswith('.pgn'):
        #     image.save(outfile, "png")
        # elif imagefile.endswith('.bmp'):
        #     image.save(outfile, "bmp")
