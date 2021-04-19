# Implement a function, so it will produce a sentence out of the given parts.
#
# Array of parts could contain:
#
# words;
# commas in the middle;
# multiple periods at the end.
# Sentence making rules:
#
# there must always be a space between words;
# there must not be a space between a comma and word on the left;
# there must always be one and only one period at the end of a sentence.
# Example:
#
# makeSentence(['hello', ',', 'my', 'dear']) // returns 'hello, my dear.'
def make_sentence(parts):
    result = ''
    for i in parts:
        if i == '.':
            result += i
            break
        elif result == '' or i == ',':
            result += i
        else:
            result += f' {i}'
    if result[-1] != '.':
        result += '.'
    return result



print(make_sentence(['hello', ',', 'my', 'dear']))

def make_sentences2(parts):
    return ' '.join(parts).replace(' ,', ',').strip(' .') + '.'


print(make_sentences2(['hello', ',', 'my', 'dear', '.', '.']))

