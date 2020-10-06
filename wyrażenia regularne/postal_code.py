import re

postal_code = re.compile(r'^[0-9]{2}-[0-9]{3}$')
p_c = postal_code.search('34-594')
print(p_c.group(0))