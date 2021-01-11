indeks = ['WIG20', 'mWIG40', 'sWIG80']
properties = ['liczba spółek', 'spółki', 'kapitalizacja']

result = {idx: {i: None for i in properties} for idx in indeks}
print(result)