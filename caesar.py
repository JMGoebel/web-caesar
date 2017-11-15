""" caesar.py:  ... """
from helpers import alphabet_position
from helpers import rotate_character

def encrypt(text, rot):
    encrypt_text = ""
    for letter in text:
        encrypt_text += rotate_character(letter, int(rot))
    return encrypt_text

def main():
    """ Entry point """
    message = input("Type a message: ")
    rotate = input("Rotate by: ")
    print(encrypt(message, rotate))

if __name__ == "__main__":
    main()
