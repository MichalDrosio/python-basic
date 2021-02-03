from itertools import permutations


def permutations2(string):
    return [''.join(p) for p in permutations(string)]



print(permutations2('ola'))


def permutations3(string):
    permutations_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            for perm in permutations3(string.replace(char, '', 1)):
                permutations_list.append(char+perm)

    return set(permutations_list)

print(permutations3('ola'))

