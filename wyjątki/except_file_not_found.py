from wyjątki.word_count import count_words

filenames = ['pliki_tekstowe/book.txt', 'pliki_tekstowe/tolkien.txt', 'hobbit.txt']
for filename in filenames:
    count_words(filename)

