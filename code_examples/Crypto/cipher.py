class Cipher:
    def __init__(self):
        self.alfa_count = 95

    def verify(self, plaintext, key):
        return self.decode(self.encode(plaintext, key), key) == plaintext