import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, s=40)
plt.title("Sześcian liczb", fontsize=24)
plt.xlabel("Wartość", fontsize=24)
plt.ylabel('Kwadrat wartości', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 140000000000])
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Oranges, edgecolors='none', s=40)
plt.show()