import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Oranges, edgecolors='none', s=1, linewidths=500)

    # punkt początkowy
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)

    # punkt końcowy
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # ukrycie osi
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # okreslenie wielkości okna
    plt.figure(figsize=(10,6))

    plt.show()

    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n):")
    if keep_running == 'n':
        break