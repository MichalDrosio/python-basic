from die_visual import frequencies
import matplotlib.pyplot as plt

x_values = list(range(1,7))
y_values = frequencies
plt.scatter(x_values, y_values, s=40)
plt.title('zuty kośćmi', fontsize=24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel('czestotliwosc wyrzucania cyfy', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 6, 0, 1000])
plt.savefig('die.png', bbox_inches='tight')