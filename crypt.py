from Crypto.Cipher import AES
import os


class Crypt(object):

    def file_crypt(self, file_str, save_to, password):
        encryption_suite = AES.new(password, AES.MODE_CFB, 'gDjeUCjdkjS7^7d#')
        crypted_file = encryption_suite.encrypt(file_str)
        crypted = open(save_to,'w')
        crypted.write(crypted_file)
        crypted.close()


class Decrypt(object):

    def file_decrypt(self, file_str, password, save_to):
        decryption_suite = AES.new(password, AES.MODE_CFB, 'gDjeUCjdkjS7^7d#')
        decrypted_file = decryption_suite.decrypt(file_str)
        decrypted = open(save_to, 'w')
        decrypted.write(decrypted_file)
        decrypted.close()

