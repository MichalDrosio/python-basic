import pygal

from roll_die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll()*die_2.roll() for roll_num in range(10000)]
print(results)

frequencies = [results.count(value) for value in range(1, (die_1.num_sides*die_2.num_sides)+1)]
print(frequencies)


hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wyniki rzutu dwiema kościami 10000 razy"
hist.x_labels = list(range(1,37))
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D6+D10', frequencies)
hist.render_to_file('dice_visual.svg')