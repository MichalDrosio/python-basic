# Mr. Square is going on a holiday. He wants to bring 2 of his favorite squares with him,
# so he put them in his rectangle suitcase.
#
# Write a function that, given the size of the squares and the suitcase,
# return whether the squares can fit inside the suitcase.
#
# fit_in(a,b,m,n)
# a,b are the sizes of the 2 squares
# m,n are the sizes of the suitcase


def fit_in(a, b, m, n):
    return max(a, b) <= min(m, n) and a + b <= max(m, n)


print(fit_in(1,2,3,2))


a = [2,34,1,4,51,3]
print(sorted(a))