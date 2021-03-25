def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)

print(binary_array_to_number([0,0,1,0]))


ar = [0,0,1,0]
ar = ar[::-1]
res = 0
for i in range( len(ar)):
    if ar[i] == 1:
        z = 2 ** i
        res += z
print(res)