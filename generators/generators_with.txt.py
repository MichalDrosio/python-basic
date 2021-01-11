def file_gen(fnames):
    for fname in fnames:
        if fname.endswith('.txt'):
            yield fname



filenames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']
print(list(file_gen(filenames)))