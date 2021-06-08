# Many people know that Apple uses the letter "i" in almost all of its devices to emphasize its personality.
#
# And so John, a programmer at Apple, was given the task of making a program that would add that letter to every word.
# Let's help him do it, too.
#
# Task:
# Your task is to make a function that takes the value of word and returns it with an "i" at the beginning of the word.
# For example we get the word "Phone", so we must return "iPhone". But we have a few rules:
#
# The word should not begin with the letter "I", for example Inspire.
# The number of vowels should not be greater than or equal to the number of consonants, for example East or Peace.
# ("y" is considered a consonant)
# The first letter should not be lowercase, for example road.
# If the word does not meet the rules, we return "Invalid word".

def i(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if not word:
        return 'Invalid word'
    else:
        word = word.lower()
        if word[0] != 'I' and word[0].isupper():
            count_vowels = 0
            for letter in vowels:
                count_vowels += word.count(letter)
            if count_vowels < len(word) - count_vowels:
                return f'i{word}'
            else:
                return 'Invalid word'
        else:
            return 'Invalid word'

# print(i('Phone'))
# print(i('World'))
# print(i('Programmer'))
# print(i(''))
# print(i('Inspire'))
# print(i('Peace'))
print(i('eEast'))