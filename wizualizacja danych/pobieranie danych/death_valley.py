import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'csv/death_valley_2014.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_data = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_data, 'Brak danych')
        else:
            dates.append(current_data)
            highs.append(high)
            lows.append(low)
print(dates)
print(lows)
print(highs)
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = "Najwyższa i najniższa temperatura dnia -2014\nDolina Śmierci , Kalifornia"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
#
# plt.show()