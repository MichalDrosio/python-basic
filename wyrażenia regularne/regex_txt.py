import re

heroRegex = re.compile(r'Batman|Tina Fey')

mo1 = heroRegex.search('Batman i Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey i Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile stracił koło')

print(mo.group())
print(mo.group(1))

batRegex2 = re.compile(r'Bat(wo)?man')
mo3 = batRegex2.search('The Adventures of Batman')
print(mo3.group())

mo4 = batRegex2.search('The Adventures of Batwoman')
print(mo4.group())

batRegex3 = re.compile(r'Bat(wo)*man')
mo5 = batRegex3.search('The Adventures of Batwowowowowoman')
print(mo5.group())

batRegex4 = re.compile(r'Bat(wo)+man')
mo6 = batRegex4.search('The Adventures of Batwoman')
print(mo6.group())


haRegex = re.compile(r'(ha){3}')
mo7 = haRegex.search('hahaha')
print(mo7.group())

haRegex2 =re.compile(r'(ha){3,5}')
mo8 = haRegex2.search('hahahahaha')
print(mo8.group())

haRegex3 = re.compile(r'(ha){3,5}?')
mo9 = haRegex3.search('hahahahaha')
print(mo9.group())


