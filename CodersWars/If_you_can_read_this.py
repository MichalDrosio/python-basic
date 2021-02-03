

nato = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India',
            'Juliett', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo',
            'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']


def to_nato(words):
    result = []
    for i in words.upper():
        if i.isalpha():
            for j in nato:
                if j[0] == i:
                    result.append(j)
        else:
            result.append(i)

    r = ' '.join(result)
    print(f'{len(r)} z spac')

    re = r.replace('  ', '')
    print(re)
    print(f'{len(re)} bez 2 spac')
    return re, r




print(to_nato('If, you can read?'))


