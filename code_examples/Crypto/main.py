from sender import Sender
from receiver import Receiver
from caesar_cipher import Caesar
from multiplication_cipher import MultiplicationCipher
from affine_cipher import AffineCipher
from unbreakable_cipher import UnbreakableCipher
from rsa_cipher import RSACipher
from hacker import Hacker


def main(cipher, rsa = 0):
    print(cipher)
    sender = Sender(cipher)
    receiver = Receiver(cipher)
    key = cipher.generate_keys()
    if rsa:
        sender.set_key(key[0])
        receiver.set_key(key[1])
    else:
        sender.set_key(key)
        receiver.set_key(key)
    message = "shady crypto"

    print("Key is: ", key)
    print("Plaintext: ", message)
    crypted = message = sender.operate_cipher(message)
    print("Cryptedtext : ", message)
    message = receiver.operate_cipher(message)
    print("Cryptedtext converted back to Plaintext: ", message)

    if cipher.verify("text hacking example", key):
        print("Cipher is verified")
    else:
        print("Cipher is invalid")

    if not rsa:
        hacker = Hacker()
        print("Hacker will hack this cryptedtext: ", crypted)
        hacked = hacker.operate_cipher(crypted, cipher)
        print("Message:", '"' + str(hacked[0]) + '"', "is hacked with Key:", hacked[1])
    print("\n"*2)

main(Caesar())
main(MultiplicationCipher())
main(AffineCipher())
main(UnbreakableCipher())
main(RSACipher(), 1)
