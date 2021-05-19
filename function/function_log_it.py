def log_it(*strings):
    path = r'C:\Users\drosi\PycharmProjects\python-podstawy\function\log_it.txt'
    with open(path, 'a') as f:
        for line in strings:
            f.write(line)
            f.write(' ')
        f.write('\n')

print(log_it('ERROR', 'Not enough data', 'invoices', '2020'))
log_it('Starting processing forecasting')