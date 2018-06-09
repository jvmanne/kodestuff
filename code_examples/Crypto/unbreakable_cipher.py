from cipher import Cipher
from random import randint


class UnbreakableCipher(Cipher):
    def __init__(self):
        super().__init__()
        self.max_key_length = 2
        self.min_key_length = 2

    def encode(self, plaintext, key):
        cryptedtext = ""
        for x in range(len(plaintext)):
            cryptedtext += chr((ord(plaintext[x]) - 32 + ord(key[x % len(key)])) % self.alfa_count + 32)
        return cryptedtext

    def decode(self, ciphertext, key):
        return self.encode(ciphertext, "".join(chr(self.alfa_count - ord(x) % self.alfa_count) for x in key))

    def generate_keys(self):
        key_length = randint(self.min_key_length, self.max_key_length)
        return "".join(chr(randint(32, 31 + self.alfa_count)) for x in range(key_length))

    def get_possible_keys(self):
        for i in range(self.min_key_length, self.max_key_length + 1):
            for j in self.get_possible_keys_of_length(i):
                yield j

    def get_possible_keys_of_length(self, i):
        for x in range(32, 127):
            if i == 1:
                yield chr(x)
            else:
                for y in self.get_possible_keys_of_length(i - 1):
                    yield chr(x) + y

    def __str__(self):
        return "Unbreakable Cipher"
