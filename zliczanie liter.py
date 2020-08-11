# Mamy podany ciąg S. Np „Ala ma kota”.
#
# 1. zliczyć wyrazy. W naszym przypadku będzie ich 3
#
# 2. zliczyć litery. Będzie ich 9
#
# 3. zbadać częstotliwość występowania liter. a – 3, l – 1, m 1, k – 1, t – 1

wyraz = 'Magda ma Michała'
words = 1
letters = 0
hash_table = {}
wyraz = wyraz.lower()
for i in wyraz:
    if i == " ":
        words += 1
    else:
        letters += 1
        if i in hash_table:
            hash_table[i] += 1
        else:
            hash_table[i] = 1
print(f"""ilosćś wyrazów:{words} 
litery:{letters}, 
ilość powtórzeń:{hash_table}""")




