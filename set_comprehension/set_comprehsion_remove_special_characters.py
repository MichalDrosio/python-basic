desc = 'Playway: Playway to company computer games.'
word_list = desc.lower().replace(':', '').replace('.', '').split()
print(word_list)
word_unique = {word for word in word_list}
print(word_unique)
print(len(word_unique))