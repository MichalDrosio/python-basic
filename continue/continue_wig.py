gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

exchange_rate = 4.0

for key, value in gaming.items():
    if value[1] == 'USD':
        value[0] = value[0] / exchange_rate
        value[1] = 'PLN'

print(gaming)

for ticker, info in gaming.items():
    if info[1] == 'PLN':
        continue
    info[0] = info[0] / 4.0
    info[1] = 'PLN'
print(gaming)