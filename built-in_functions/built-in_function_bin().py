number = 100
print(bin(number))
binary = bin(number)

binary = binary[2:]
print(type(binary))
print(binary)
print(binary.count('1'))