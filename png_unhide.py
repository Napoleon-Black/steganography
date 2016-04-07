# -*- coding: utf8 -*-

from PIL import Image
from itertools import product

class UnhideMessage(object):
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
        
        return ''.join(message)

unhide = UnhideMessage()
a = unhide.unhide_message('hide_image.png')
print a
