with open('pliki tekstowe/plw_d.csv', 'r') as file:
    content = file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[4]) for line in content]

print(data)
result = {
    data[0][0]: [data[1:][i][0] for i in range(len(data)-1)],
    data[0][1]: [data[1:][i][1] for i in range(len(data)-1)]
}
print(result)

volumes = [line.split(',')[-1] for line in content][1:]
print(volumes)
volumes = [int(vol) for vol in volumes]
max_vol = max(volumes)
print(max_vol)



days = [(line.split(',')[0], line.split(',')[-1]) for line in content][1:]
days = [(val[0], int(val[1])) for val in days]
max_vol = max([val[1] for val in days])
max_date = list(filter(lambda val: val[1] == max_vol, days))[0][0]
print(f'Data: {max_date}')