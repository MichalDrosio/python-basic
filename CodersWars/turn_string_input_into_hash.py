# Please write a function that will take a string as input and return a hash. The string will be formatted as such.
# The key will always be a symbol and the value will always be an integer.
#
# "a=1, b=2, c=3, d=4"
# This string should return a hash that looks like
#
# { 'a': 1, 'b': 2, 'c': 3, 'd': 4}

# def str_to_hash(st):
#     d = {}
#     st = st.split(',')
#     print(st)
#     for s in st:
#         le = ''
#         di = ''
#         for i in s:
#             if i.isalpha():
#                 le += i
#             elif i.isdigit():
#                 di += i
#             else:
#                 continue
#         d[le] = int(di)
#     return d

def str_to_hash(st):
    result = {}

    if st:
        for i in st.split(', '):
            value = i.split('=')
            result[value[0]] = int(value[1])

    return result
print(str_to_hash('aws=1, b=2, c=3, d=4'))