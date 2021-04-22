# Your task is to write a function called valid_spacing() or validSpacing() which checks if a string has valid spacing.
# The function should return either True or False.
#
# For this kata, the definition of valid spacing is one space between words, and no leading or trailing spaces.
# Below are some examples of what the function should return.
#
# 'Hello world' = True
# ' Hello world' = False
# 'Hello world  ' = False
# 'Hello  world' = False
# 'Hello' = True
# # Even though there are no spaces, it is still valid because none are needed
# 'Helloworld' = True
# # True because we are not checking for the validity of words.
# 'Helloworld ' = False
# ' ' = False
# '' = True

def valid_spacing(string):
    if string == '':
        return True
    elif string == ' ':
        return False
    for i in range(len(string)-1):
        if string[0] == ' ' or string[-1] == ' ':
            return False
        elif string[i] == ' ':
            if string[i] == string[i+1]:
                return False
    return True


def valid_spacing(s):
    print(s.split())
    return s == ' '.join(s.split())


print(valid_spacing('Hello  world'))
print(valid_spacing(''))
print(valid_spacing(' '))