# Write a program which accepts a sequence of words separated by whitespace
# as input to print the words composed of digits only.

import re

words = input('slowa:\n')
print(re.findall('\d+', words))
p = []
for i in words:
    try:
        a = int(i)
        p.append(a)
    except ValueError:
        pass
print(p)
