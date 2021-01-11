stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
result = {k: v for k, v in stocks.items() if v > 100}
print(result)