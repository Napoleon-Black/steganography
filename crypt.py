# -*- coding: utf-8 -*-

import os 
import hashlib

from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish


class Crypt(object):

    #AES Encryption
    def file_crypt(self, file_str, set_image, save_to, password,
                   image_type, file_name):

        password = hashlib.sha256(password).digest() #password hash
        encryption_suite = AES.new(password, AES.MODE_CFB, '^#%!8&8@4-)*Dnj0')
        crypted_file = encryption_suite.encrypt(file_str)
        import hide
        hide = hide.HideMessage()
        hide.hide_message(crypted_file, set_image, save_to,
                          image_type, file_name)

    #Blowfish Encryption
    def blowfish_file_crypt(self, file_str, set_image, save_to, password,
                            image_type, file_name):

        password = hashlib.sha256(password).digest()
        encryption_suite = Blowfish.new(password, Blowfish.MODE_CFB, '&)#(%&7h')
        crypted_file = encryption_suite.encrypt(file_str)
        import hide
        hide = hide.HideMessage()
        hide.hide_message(crypted_file, set_image, save_to,
                          image_type, file_name)


class Decrypt(object):

    #AES Decryption
    def file_decrypt(self, image_file, password, save_to, image_type):

        password = hashlib.sha256(password).digest() #password hash
        import unhide
        unhide = unhide.UnhideMessage()
        unhided_file = unhide.unhide_message(image_file, image_type)
        decryption_suite = AES.new(password, AES.MODE_CFB, '^#%!8&8@4-)*Dnj0')
        decrypted_file = decryption_suite.decrypt(unhided_file[1])
        decrypted = open(save_to + '/' + unhided_file[0], 'w')
        decrypted.write(decrypted_file)
        decrypted.close()

    #Blowfish Decryption
    def blowfish_file_decrypt(self, image_file, password, save_to, image_type):

        password = hashlib.sha256(password).digest()
        import unhide
        unhide = unhide.UnhideMessage()
        unhided_file = unhide.unhide_message(image_file, image_type)
        decryption_suite = Blowfish.new(password, Blowfish.MODE_CFB, '&)#(%&7h')
        decrypted_file = decryption_suite.decrypt(unhided_file[1])
        decrypted = open(save_to + '/' + unhided_file[0], 'w')
        decrypted.write(decrypted_file)
        decrypted.close()
        


