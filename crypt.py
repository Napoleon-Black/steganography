from Crypto.Cipher import AES


class Crypt(object):
    key = ''
    
    def input(self):
        input_file = open('test.txt', 'r')
        file_str = input_file.read()
        self.file_crypt(file_str)

    def enter_key(self):
        user_key = ''
        while len(user_key) != 16:
            user_key = str(raw_input('Enter your key: '))
        self.key = user_key
        return user_key

    def file_crypt(self, file_str):
        encryption_suite = AES.new(self.enter_key(), AES.MODE_CFB, 'gDjeUCjdkjS7^7d#')
        crypted_file = encryption_suite.encrypt(file_str)
        crypted = open('crypted','w')
        crypted.write(crypted_file)
        crypted.close()

crypt = Crypt()
crypt.input()

class Decrypt(object):

    def input(self):
        input_file = open('crypted', 'r')
        file_str = input_file.read()
        self.file_decrypt(file_str)

    def enter_key(self):
        user_key = ''
        while len(user_key) != 16:
            user_key = str(raw_input('Enter your key: '))
        return user_key

    def file_decrypt(self, file_str):
        decryption_suite = AES.new(self.enter_key(), AES.MODE_CFB, 'gDjeUCjdkjS7^7d#')
        decrypted_file = decryption_suite.decrypt(file_str)
        decrypted = open('decrypted.txt', 'w')
        decrypted.write(decrypted_file)
        decrypted.close()

decrypt = Decrypt()
decrypt.input()