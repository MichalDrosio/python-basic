hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = True
for h in hashtags:
    if not isinstance(hashtags, str):
        result = False
        break

print(result)
