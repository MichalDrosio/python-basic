import re

postal_code = re.compile(r'^\d{2}-\d{3}$')
p_c = postal_code.search('34-594')
print(p_c.group(0))