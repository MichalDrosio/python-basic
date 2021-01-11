from collections import Counter

items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']

counter = Counter()
for item in items:
    counter[item] += 1

print(counter)