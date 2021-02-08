# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
# For example:
#
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"


import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

x = domain_name("http://github.com/carbonfive/raygun")
y = domain_name("http://www.zombie-bites.com")
z = domain_name("https://www.cnet.com")
print(x)
print(y)
print(y)

print(f'{10**0}%{13}={(10**6)%13}')