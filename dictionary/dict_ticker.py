ticker = [
   'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
   'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
   'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
   'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]

print(list(enumerate(ticker)))
d = {}
for i in range(len(ticker)):
    d[i] = ticker[i]
print(list(d.items()))
print(d)
print(dict(enumerate(ticker)))