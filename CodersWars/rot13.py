# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters
# after it in the alphabet. ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
import string

def rot13(message, key):
    word = ''
    for letter in message:
        if letter.isalpha():
            num = ord(letter)
            num += key
            if letter.isupper():
                if num > 90:
                    num -= 26
            else:
                if num > 122:
                    num -= 26
            word += chr(num)
        else:
            word += letter
    return word

print(rot13('Test', 13))


