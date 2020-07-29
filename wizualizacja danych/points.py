import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=40, edgecolors='none', c=y_values, cmap=plt.cm.Reds)
plt.title('Kwadraty liczb', fontsize=24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel('Kwadraty wartości', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')