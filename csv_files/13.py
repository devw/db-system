import numpy as np
import matplotlib.pyplot as plt

num_rolls = 1000
num_dies = 3
dice_rolls = np.random.randint(1, 7, size =(num_rolls, num_dies))
sums = [x.sum() for x in dice_rolls]
print(sums)

plt.hist(sums, bins=range(0,20), color='#00ff00')

plt.show()
