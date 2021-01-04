text = 'Python jest bardzo polularnym jęykiem programowania'
result = []
words = text.split(' ')
for i in words[:4]:
    result.append(i.lower())
print(result)

res = []
for idx, word in enumerate(words):
    if idx < 4:
        res.append(word.lower())
print(res)