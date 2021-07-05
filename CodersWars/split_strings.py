# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then
# it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']


def solution(s):
    result = []
    i = 0
    while i < len(s):
        char = s[i:i+2]
        if len(char) < 2:
            char += '_'
        i += 2
        result.append(char)
    return result

print(solution("asdfadsf"))
print(solution("asdfads"))