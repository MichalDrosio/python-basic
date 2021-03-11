# Your task is to sort a given string. Each word in the string will contain a single number.
# This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.


# def order(sentence):
#     r = []
#     array = sentence.split(' ')
#     print(array)
#     for word in array:
#         for num in word:
#             try:
#                 num = int(num)
#                 r.append((num, word))
#             except ValueError:
#                 pass
#     x = sorted(r, key=lambda item: item[0])
#     result = []
#     for i in x:
#         result.append(i[1])
#     return ' '.join(result)

# def order(sentence):
#     if not sentence:
#         return ""
#     result = []
#
#     split_up = sentence.split()
#
#     for i in range(1, 10):
#         for item in split_up:
#             if str(i) in item:
#                 result.append(item)
#
#     return " ".join(result)


def extract_number(word):
    for l in word:
        if l.isdigit():
            print(l)
            return l
    return None

def order(sentence):
    s = sentence.split()
    ss = sorted(s, key=extract_number)
    print(ss)
    return ' '.join(sorted(sentence.split(), key=extract_number))


print(order("is2 Thi1s T4est 3a"))