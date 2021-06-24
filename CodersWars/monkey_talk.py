# Lets talk like a monkey. Find out how! Look at the test cases an engineer code to pass them.

def monkey_talk(phrase):
    result = []
    marks = 'aeiouAEIOU'
    for word in phrase.split():
        if word[0] in marks:
            result.append('eek')
        else:
            result.append('ook')
    return f'{" ".join(result).capitalize()}.'

print(monkey_talk('Hello'))
print(monkey_talk('Everyone'))
print(monkey_talk('Hello Everyone'))
print(monkey_talk('Everyone Hello'))