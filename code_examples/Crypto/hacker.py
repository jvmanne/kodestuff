from person import Person


class Hacker(Person):
    def __init__(self):
        pass

    def operate_cipher(self, ciphertext, cipher):
        with open("WordList", "r") as word_list:
            words = list(map(str.strip, word_list.readlines()))
        bestkey = ""
        bestkeyscore = 0
        for key in cipher.get_possible_keys():
            plaintext = cipher.decode(ciphertext, key)
            plainlist = plaintext.split(" ")
            keyscore = 0
            for word in plainlist:
                if word in words:
                    keyscore += len(word)
            if keyscore > bestkeyscore:
                bestkey = key
                bestkeyscore = keyscore
        return cipher.decode(ciphertext, bestkey), bestkey