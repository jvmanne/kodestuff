from cipher import Cipher
from crypto import generate_random_prime, modular_inverse, blocks_from_text, text_from_blocks
from random import randint
from math import gcd


class RSACipher(Cipher):
    def __init__(self):
        super().__init__()
        self.b = 8
        self.l = 1

    def encode(self, plaintext, key):
        blocks = blocks_from_text(plaintext, self.l)
        return [pow(x, key[1], key[0]) for x in blocks]

    def decode(self, ciphertext, key):
        blocks = [pow(x, key[1], key[0]) for x in ciphertext]
        return text_from_blocks(blocks, self.l)

    def generate_keys(self):
        while 1:
            p, q = generate_random_prime(self.b), generate_random_prime(self.b)
            if p != q:
                break
        n = p * q
        phi = (p - 1) * (q - 1)
        while 1:
            e = randint(3, phi - 1)
            if gcd(e, phi) == 1:
                break
        d = modular_inverse(e, phi)
        return [(n, e), (n, d)]

    def verify(self, plaintext, key):
        return self.decode(self.encode(plaintext, key[0]), key[1]) == plaintext

    def __str__(self):
        return "RSA Cipher"