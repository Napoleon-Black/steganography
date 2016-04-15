from Crypto.Cipher import AES
import os, hashlib



class Crypt(object):

    def file_crypt(self, file_str, set_image, save_to, password):
        password = hashlib.sha256(password).digest()
        encryption_suite = AES.new(password, AES.MODE_CFB, '0000000000000000')
        crypted_file = encryption_suite.encrypt(file_str)
        import png_hide
        hide = png_hide.HideMessage()
        hide.hide_message(crypted_file, set_image, save_to)


class Decrypt(object):

    def file_decrypt(self, image_file, password, save_to):
        password = hashlib.sha256(password).digest()
        import png_unhide
        unhide = png_unhide.UnhideMessage()
        unhided_file = unhide.unhide_message(image_file)
        decryption_suite = AES.new(password, AES.MODE_CFB, '0000000000000000')
        decrypted_file = decryption_suite.decrypt(unhided_file)
        decrypted = open(save_to, 'w')
        decrypted.write(decrypted_file)
        decrypted.close()
        


