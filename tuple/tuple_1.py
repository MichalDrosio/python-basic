wig = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')
result = wig + mwig40
result2 = (wig, mwig40)
print(result)
print(result2)

members = (('Kasia', 23), ('Tomek', 19))
person = ('Adam', 26)
result3 = (members[0], person, members[1])
print(result3)

defalut = ('YES', 'NO', 'NO', 'YES', 'NO')
print(defalut.count('YES'))

names = ('Ola', 'Monika', 'Tomek', 'Olaf', 'Adam')
sorted_names = tuple(sorted(names))
print(sorted_names)

info = (('MOnika', 19), ('Tomek', 21), ('Adam', 18), ('Jarek', 30))
asc_info = tuple(sorted(info, key=lambda item: item[1]))
desc_info = tuple(sorted(info, key=lambda item: item[1], reverse=True))
print(asc_info)
print(desc_info)

stocks = (('Playway', ('PLW', 310)), ('CD Projekt', ('CDR', 300)))
print(stocks[0][1][0])
