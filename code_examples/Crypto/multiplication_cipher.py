from cipher import Cipher
from crypto import modular_inverse
from random import randint
from math import gcd

class MultiplicationCipher(Cipher):
    def __init__(self):
        super().__init__()

    def encode(self, plaintext, key):
        cryptedtext = ""
        for x in plaintext:
            cryptedtext += chr((ord(x) - 32) * key % self.alfa_count + 32)
        return cryptedtext

    def decode(self, ciphertext, key):
        return self.encode(ciphertext, modular_inverse(key, self.alfa_count))

    def generate_keys(self):
        while 1:
            key = randint(1, self.alfa_count)
            if gcd(key, self.alfa_count) == 1:
                return key

    def get_possible_keys(self):
        for i in range(1, self.alfa_count):
            if gcd(i, self.alfa_count) == 1:
                yield i

    def __str__(self):
        return "Multiplication Cipher"