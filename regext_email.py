# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.

import re

email = input('email')
pat = '(\w+)@((\w+\.)+(com))'
r = re.match(pat, email)
print(r.group(1))
print(r.group(2))
