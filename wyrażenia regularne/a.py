import re
# "." - zamiast kropiki mozemy wstawic dowolny znak
# "[]" - dowolna ilosc znakow miedzy nawiasami
# "[^]" - znaki nie wymienione miedzy nawiasami
# "*" - wszystkie kombinacje znaków

inscription = 'Michal lubi grac w pilke'
if re.match('lubi', inscription):
    print('jest')

if re.search('lubi', inscription):
    print('yes')

if re.search('lu.i', inscription):
    print('y')

if re.search('[alsbdh]u.i', inscription):
    print('qwerty')

expression = re.compile('l[^ ]*')
for i in re.findall(expression, inscription):
    print(i, end=' ')