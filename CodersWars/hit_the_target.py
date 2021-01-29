# Hit the target
# given a matrix n x n (2-7), determine if the arrow is directed to the target (x).
# There will be only 1 arrow '>' and 1 target 'x'
# An empty spot will be denoted by a space " ", the target with a cross "x", and the scope ">"

matrix = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', '>', ' ', 'x'],
    [' ', ' ', ' ', ' ']
]


def solution(mtrx):
    for index in mtrx:
        if '>' in index and 'x' in index:
            return index.index('>') < index.index('x')
    return False


print(solution(matrix))