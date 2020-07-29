with open('pliki tekstowe/python') as file_object:
    odczyt = file_object.read()
    print(odczyt)
    print('-'*100)

file = 'pliki tekstowe/python'
with open(file) as file_object:
    for i in file_object:
        print(i.strip())
    print('-' * 100)

with open(file) as file_object:
    lines = file_object.readlines()
    print(lines)

for line in lines:
    print(line.strip())
    sas = line.replace('Python', "SAS")
    if "SAS" in sas:
        print(sas)
