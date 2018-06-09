from person import Person

class Receiver(Person):
    def __init__(self, cipher):
        super().__init__(cipher)

    def operate_cipher(self, ciphertext):
        return self.cipher.decode(ciphertext, self.key)