def count_words(filename):
    try:
        with open(filename) as file_objects:
            contents = file_objects.read()
            words = contents.split()
            num_words = len(words)
            print(f'Plik {filename} zawiera {num_words} słów')
    except FileNotFoundError:
        pass


