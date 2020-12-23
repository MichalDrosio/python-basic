przedmioty = {'matematyka', 'polski'}
przedmioty.add('angielski')
print(przedmioty)
print(type(przedmioty))

text = 'Programing in python'
text = text.lower().replace(' ', '').replace('.', ' ')

print(text)
letters = set(text)
print(letters)
vowels = {'a', 'e', 'i', 'o', 'u'}


consonants = letters.difference(vowels)
print(consonants)

for i in vowels:
    if i in letters:
        letters.remove(i)
print(letters)


A = {2, 4, 6, 8}
B = {4, 10}
sum_diff = A.symmetric_difference(B)
print(sum_diff)


ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}
result = ad1_id.symmetric_difference(ad2_id)
print(result)

is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
res = is_clicked.intersection(is_bought)
print(res)


