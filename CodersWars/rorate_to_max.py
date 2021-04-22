def max_rot(n):
    s = str(n)
    arr = n
    for i in range(len(s)):
        s = s[:i] + s[i+1:] + s[i]
        print(s)
        if arr < int(s):
            arr = int(s)
    return arr

print(max_rot(56789))



