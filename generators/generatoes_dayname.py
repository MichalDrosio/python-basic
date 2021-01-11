def dayname(index):
    days = ['pon', 'wt', 'śr', 'czw', 'pt', 'sb', 'nd']
    yield days[index - 1]
    yield days[index]
    yield days[(index + 1) % 7]

