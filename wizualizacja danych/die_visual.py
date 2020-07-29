from roll_die import Die
import pygal

die = Die()

results = [die.roll() for roll_num in range(1000)]

print(results)

frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

print(frequencies)

hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wyniki rzutu kąstką 10000 razy"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')