# Gordon Ramsay shouts. He shouts and swears. There may be something wrong with him.
#
# Anyway, you will be given a string of four words. Your job is to turn them in to Gordon language.
#
# Rules:
#
# Obviously the words should be Caps, Every word should end with '!!!!',
# Any letter 'a' or 'A' should become '@', Any other vowel should become '*'.

def gordon(a):
    x = ('e', 'o', 'u')
    y = ('a',)
    res = ''
    for i in a:
        if i.lower() in x:
            res += '*'
        elif i.lower() in y:
            res += '@'
        elif i == ' ':
            res += '!!!! '
        else:
            res += i.upper()
    res += '!!!!'
    return res

print(gordon('What feck damn cake'))