  # Zadanie jest następujące. Przy użyciu języka Python, należy znaleźć najmniejszą oraz największa liczbę na liście.
# Czyli, dla przykładu, jeżeli nasza lista to:

lista = [1,4,-4,7]
print('min:',min(lista),'max:',max(lista))

najmniejsza = None
najewieksza = None

for i in lista:
    if najmniejsza == None or najmniejsza > i:
        najmniejsza = i
    if najewieksza == None or najewieksza < i:
        najewieksza = i

print(f'najwieksza:{najewieksza}, najmniejsza:{najmniejsza}')