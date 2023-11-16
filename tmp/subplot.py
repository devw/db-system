import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
x =[x / 10 for x in range(-100, 100) ]
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x
y4 = [x ** 2 for x in x]


# Create a 2x2 grid of subplots
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title('Subplot 1')

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title('Subplot 2')

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title('Subplot 3')

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title('Subplot 4')

plt.tight_layout()  # Improves spacing between subplots

plt.show()






