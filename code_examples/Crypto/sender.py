from person import Person

class Sender(Person):
    def __init__(self, cipher):
        super().__init__(cipher)

    def operate_cipher(self, plaintext):
        return self.cipher.encode(plaintext, self.key)