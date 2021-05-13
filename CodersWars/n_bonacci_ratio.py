# The Fibonacci sequence is the sequence that starts with 0, 1
# that increases by the previous two terms added together each time.
# In mathematical terms:
# F(0) = 0	F(1) = 1	F(x) = F(x-1) + F(x-2)
# As the number of terms approaches infinity, the ratio between
# the last term and the term before that approaches a constant. This is known as the golden ratio.
# It is approximately equal to 1.61803.
# There is another sequence called the Pell Sequence (or the two-bonacci sequence),
# which is very similar to the Fibonacci sequence:
# P(0) = 0	P(1) = 1	P(x) = 2 * P(x-1) + P(x-2)
# The ratio between the last two numbers as the length of the sequence approaches infinity also approaches a constant:
# approximately 2.4142. This is known as the silver ratio.


def n_bonacci_ratio(n):
    a, b = 0, 1
    for i in range(20):
        a, b = b, n * b + a
    return b / a

print(n_bonacci_ratio(95))



