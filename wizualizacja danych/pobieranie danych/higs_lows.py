import csv
from matplotlib import pyplot as plt
from countdown import datetime

filename = 'csv/sitka_weather_07-2014.csv'
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)
    # print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    highs = []
    dates = []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
    print(highs)


fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red')

plt.title("Najwyższa temperatura dnia, lipiec 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16 )

plt.show()