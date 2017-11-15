''' helper functions for caesar and vigenere cyphers '''

def alphabet_position(letter):
    ''' Return the ordinal position of a character '''
    return ord(letter.lower()) - 97

def rotate_character(char, rot):
    ''' Finds the character (rot) positions to the right '''
    return chr(((alphabet_position(char) + rot) % 26)
               + (97 if char.islower() else 65)) if char.isalpha() else char
