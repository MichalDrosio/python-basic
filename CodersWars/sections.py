# Consider the following equation of a surface S: z*z*z = x*x * y*y.
# Take a cross section of S by a plane P: z = k where k is a positive integer (k > 0).
# Call this cross section C(k).
#
# Task
# Find the number of points of C(k) whose coordinates are positive integers.
#
# Examples
# If we call c(k) the function which returns this number we have
#
# c(1) -> 1
# c(4) -> 4
# c(4096576) -> 160
# c(2019) -> 0 which means that no point of C(2019) has integer coordinates.
# Notes
# k can go up to about 10,000,000,000
# Prolog: the function cis called section.
# Please could you ask before translating : some translations are already written.


def c(k):
    n = int(k**0.5)
    r = 1
    if n*n != k:
        return 0
    else:
        for i in range(2, n+1):
            if n%i != 0:
                continue
            else:
                c = 0
                while n%i == 0:
                    n /= i
                    c += 1
                r *= (c-1)*3 +4
        return r

print(c(1369))