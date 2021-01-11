import re
string = 'Python 3.8'
result = re.findall(pattern=r'\d',string=string)
print(result)

string_2 = '!@#$%^&45wc'
result_2 = re.findall(pattern=r'\w', string=string_2)
print(result_2)

raw_text = "Wyślij email na adres: info@template.com lub sales-info@template.it"
result_3 = re.findall(r'[\w\.-]+@[\w\.-]+', raw_text)
print(result_3)


text = 'Programowanie w języku Python - od A do Z'
result_4 = re.split(pattern=r'\s+', string=text)
print(result_4)