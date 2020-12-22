filename = 'michal'
print(filename[-3:])
print(filename[5:])

string = 'PKV-89415-PLN'
code = string[:3] + string[-3:]
print(code)

num = '1 0 0 1 0 1'
binary = num[::2]
print(binary)
number = int(binary, 2)
print(number)


text = 'Kurs python'
print(text[::-1])

flag = '23'
print(isinstance(flag, str))

text = 'python jest popularnym jezykiem programowania'
print(text.title())
print(text.capitalize())
p = 0
print(text.count('p'))
for i in text:
    if i == 'p':
        p += 1
print(p)

code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'
print(code1.endswith('2020'))
print(code2.endswith('2020'))
path1 = 'youtube.com/watch'
path2 = 'google.com/search/'
print(path1.startswith('youtube'))
print(path2.startswith('youtube'))
print(path1.find('com'))
print(path2.find('arch'))

c1 = 'FVNISJND-20'
c2 = 'FVNISJND20'
print(c1.isalnum())
print(c2.isalnum())

txt = '  Google Colab  '
print(txt.strip())

code3 = 'FVNISJND-XX'
print(code3.replace('-', ' '))

numbers = '340-23-987-123'
print(numbers.replace('-', ''))

txt2 = 'Open,High,Low,Close'
print(txt2.split(','))

txt3 = """Python jest językiem ogólnego przeznaczenia.
Python jest popularny"""
print(txt3.splitlines())

num2 = 34
print(str(num2).zfill(6))

