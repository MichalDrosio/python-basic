# Your mission is to list all possible match flows with scores up to k (k is a parameter).
# Meaning the first to reach k points wins the match.
#
# For examples, Table Tennis (Ping-pong) is a game with 11-point system (up to 11).
#
# In this kata your mission is to write a function getting a positive integer value k>0 and it should
# return all possible match flows up to score of k. Players' scores can increment by one only.
#
# NOTE: Pay attention to the order of possible matches.

# The required order of matches is actually all the paths from root to leaves, from left to right.
# In every node we go to the left option and then the right one.
#
# Example 1
# There are 2 possible matches up to score of k=1:
#
# [['0:0', '1:0'], ['0:0', '0:1']]
#
# Example 2
# There are 6 possible matches up to score of k=2:
#
# [['0:0', '1:0', '2:0'], ['0:0', '1:0', '1:1', '2:1'], ['0:0', '1:0', '1:1', '1:2'], ['0:0', '0:1', '1:1', '2:1'],
# ['0:0', '0:1', '1:1', '1:2'], ['0:0', '0:1', '0:2']]



def generate_all_possible_matches(k):
    Q = [[(0, 0)]]
    Z = []
    while Q:
        L = Q.pop()
        p, q = L[-1]
        for i in (0, 1):
            T = (p + (i == 0), q + (i == 1))
            if k in T:
                Z += [L + [T]]
            else:
                Q += [L + [T]]
    return [[f'{b}:{a}' for a, b in R] for R in sorted(Z)]


print(generate_all_possible_matches(2))