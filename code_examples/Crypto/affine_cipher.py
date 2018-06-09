from cipher import Cipher
from multiplication_cipher import MultiplicationCipher
from caesar_cipher import  Caesar


class AffineCipher(Cipher):
    def __init__(self):
        super().__init__()
        self.multiplication = MultiplicationCipher()
        self.caesar = Caesar()

    def encode(self, plaintext, key):
        return self.caesar.encode(self.multiplication.encode(plaintext, key[0]), key[1])

    def decode(self, ciphertext, key):
        return self.multiplication.decode(self.caesar.decode(ciphertext, key[1]), key[0])

    def generate_keys(self):
        return (self.multiplication.generate_keys(), self.caesar.generate_keys())

    def get_possible_keys(self):
        for key1 in self.multiplication.get_possible_keys():
            for key2 in self.caesar.get_possible_keys():
                yield key1, key2

    def __str__(self):
        return "Affine Cipher"