# Task:
# You are given a word target and list of sorted(by length(increasing), number of upper case letters(decreasing),
# natural order) unique words words which always contains target,
# task is to find the index(0 based) of target in words,which would always be in the list.
#
# Examples:
# words = ['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh', 'codewars']
# '''
# (list is sorted by length(small to big), then by number of uppercase letters(maximum to minimum)
# and then by natural order)
# '''
# target = 'codewars'
# #result should be 7
#
# #Another example:
# words = ['cP', 'rE', 'sZ', 'am', 'bt', 'ev', 'hq', 'rx', 'yi', 'akC', 'nrcVpx', 'iKMVqsj']
# target = 'akC'
# #result should be 9

def index_of(words, target):
    key = lambda w: (len(w), -sum(x.isupper() for x in w), w)
    t = key(target)
    a, b = 0, len(words) - 1
    while a < b:
        m = a + b >> 1
        k = key(words[m])
        if k < t:
            a = m + 1
        elif k > t:
            b = m
        else:
            return m
    return a
print(index_of(['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh', 'codewars', 'codewarsss'],
               'codewars'))
print(index_of(['cP', 'rE', 'sZ', 'am', 'bt', 'ev', 'hq', 'rx', 'yi', 'akC', 'nrcVpx', 'iKMVqsj'], 'akC'))
