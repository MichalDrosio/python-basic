# We have a square matrix M of dimension n x n that has positive and negative numbers in the ranges
# [-9,-1] and [0,9],( the value 0 is excluded).
#
# We want to add up all the products of the elements of the diagonals UP-LEFT to DOWN-BOTTOM, that is the value ofsum1;
# and the elements of the diagonals UP-RIGHT to LEFT-DOWN and that is sum2.
# Then, as a final result, the value of sum1 - sum2.
#
# E.g.
#
M = [[ 1,  4, 7,  6,  5],
     [-3,  2, 8,  1,  3],
     [ 6,  2, 9,  7, -4],
     [ 1, -2, 4, -2,  6],
     [ 3,  2, 2, -4,  7]]

def sum_prod_diags(m):
    s = 0
    n = len(m)
    for d in 0, -1:
        for x in range(n):
            h = v = 1
            for u in range(n-x):
                h *= m[u ^ d][x+u]
                if x: v *= m[(x+u) ^ d][u]
            s += (d | 1) * (h + v)
    return s





print(sum_prod_diags(M))