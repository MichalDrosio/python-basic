# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106



a = input()
n1 = int( "%s" % a )

n2 = int( "%s%s" % (a,a) )

n3 = int( "%s%s%s" % (a,a,a) )

n4 = int( "%s%s%s%s" % (a,a,a,a) )

print (n1+n2+n3+n4)

num1 = a
num2 = 2*a
num3 = 3*a
num4 = 4*a
result = int(n1)+int(n2)+int(n3)+int(n4)
print(result)