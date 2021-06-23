# In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.
#
# For example:
#
# dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].
# dup(["kelless","keenness"]) = ["keles","kenes"].
# Strings will be lowercase only, no spaces. See test cases for more examples.

def dup(array):
    result = []

    for word in array:
        i = 1
        text = ''
        while i < len(word):
            if word[i] == word[i-1]:
                i += 1
                continue
            else:

                text += word[i]
                i += 1
        text = word[0] + text
        result.append(text)

    return result


print(dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]))