stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}

print(stocks['PLW'])
print(stocks.get('TEN').get('Ten Square Games'))
print(stocks['TEN']['Ten Square Games'])

stocks['CDR']['CD Projekt'] = 301
print(stocks['CDR'])

stocks['BBT'] = {'Boombit': 23}
print(stocks)