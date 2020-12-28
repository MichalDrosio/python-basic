cities = ['Warszawa', 'Siedlce', 'Gdynia']
cities.append('Kraków')
print(cities)

idx = ['001', '002', '001', '003', '001']
print(idx.count('001'))

text = 'Programowanie w języku Python'
text = text.lower()
text = text.replace('ę', 'e')
array_marks = []
for i in text:
    if i not in array_marks and i != ' ':
        array_marks.append(i)
print(array_marks)
array_marks.sort()
marks = list(set(text))
print(marks)
marks.remove(' ')
marks.sort()
print(marks[:10])
print(array_marks[:10])

filenames = ['view.jpg', 'bear.jpg', 'ball.jpg']
filenames.insert(0, 'phone.jpg')
filenames.remove('ball.jpg')
print(filenames)

day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day1.extend(day2)
print(day1)

techs = ('python', 'java', 'sql', 'aws')
techs = tuple(sorted(techs))
print(techs)

hashtags = ['summer', 'time', 'vibes']
print('#'+'#'.join(hashtags))
