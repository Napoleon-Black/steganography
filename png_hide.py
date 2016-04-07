# -*- coding: utf8 -*-

from PIL import Image
from itertools import product

class HideMessage(object):

    def bin_message(self,):
        print (message)
        messagelen = len(message)
        print (messagelen)
        binlen = bin(messagelen)[2:]
        print (binlen)
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
        binmessage = bin_message(message)
        image = Image.open(imagefile)
        pix = image.load()
        sizex, sizey = image.size
        nextindex = product(range(sizex), range(sizey))
        for m in binmessage:
            index = next(nextindex)
            r, g, b, a = pix[index]
            lastbit = bin(b)[-1:]
            if m == '0':
                if lastbit == '1':
                    b -= 1
            elif m == '1':
                if lastbit == '0':
                    b += 1
        
            pix[index] = r,g,b,a
    
        image.save(outfile)

