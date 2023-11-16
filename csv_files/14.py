import numpy as np
import matplotlib.pyplot as plt

dice_rolls = np.random.randint(1, 7, size=100000)
print(dice_rolls)

plt.subplot(2, 1, 1)
plt.hist(dice_rolls, bins=[ x - .5 for x in range(1,8)], edgecolor="#33ff55")



dice_rolls = np.random.randint(1, 7, size=(100000, 3))
# print(dice_rolls)
dice_rolls_sum = [x.sum() for x in dice_rolls]
# print(dice_rolls_sum)

plt.subplot(2, 1, 2)
plt.hist(dice_rolls_sum, bins=[ x - .5 for x in range(3,19)], edgecolor="#33ff55")


plt.show()
