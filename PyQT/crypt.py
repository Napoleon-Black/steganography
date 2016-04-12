from Crypto.Cipher import AES
import os



class Crypt(object):

    def file_crypt(self, file_str, set_image, save_to, password):
        encryption_suite = AES.new(password, AES.MODE_CFB, 'gDjeUCjdkjS7^7d#')
        crypted_file = encryption_suite.encrypt(file_str)
        import png_hide
        hide = png_hide.HideMessage()
        hide.hide_message(image_name, crypted_file, set_image, save_to)


class Decrypt(object):

    def file_decrypt(self, image_file, password, save_to):
        import png_unhide
        unhide = png_unhide.UnhideMessage()
        unhided_file = unhide.unhide_message(image_file)
        decryption_suite = AES.new(password, AES.MODE_CFB, 'gDjeUCjdkjS7^7d#')
        decrypted_file = decryption_suite.decrypt(unhided_file)
        decrypted = open(save_to, 'w')
        decrypted.write(decrypted_file)
        decrypted.close()
        


