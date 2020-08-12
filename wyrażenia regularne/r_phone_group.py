import re

number = re.compile(r'(\d{2}-)?(\d{3}-\d{3}-\d{3})')
my_num = number.search('moj nr tel to 48-345-234-124')
you_num = number.search('moj nr tel to 345-234-124')
print(my_num.group(1), my_num.group(2))
print(my_num.groups())

print(you_num.groups())
print(you_num.group())