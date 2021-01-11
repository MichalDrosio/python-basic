import random

random.seed(15)

items = ['python', 'java', 'sql', 'c++', 'c']

print(random.choice(items))

random.shuffle(items)
print(items)