from cipher import Cipher
from random import randint


class Caesar(Cipher):
    def __init__(self):
        super().__init__()

    def encode(self, plaintext, key):
        crypted = ""
        for x in plaintext:
            crypted += chr((ord(x) + key - 32) % self.alfa_count + 32)
        return crypted

    def decode(self, ciphertext, key):
        return self.encode(ciphertext, self.alfa_count - key)

    def generate_keys(self):
        return randint(1, self.alfa_count - 1)

    def get_possible_keys(self):
        for i in range(1, self.alfa_count):
            yield i

    def __str__(self):
        return "Caesar Cipher"