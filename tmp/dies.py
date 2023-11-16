import numpy as np
import matplotlib.pyplot as plt

# Simulate rolling a fair six-sided die 1000 times and sum the results
num_rolls = 1000
num_dice = 3
dice_rolls = np.random.randint(1, 7, size=(num_rolls, num_dice))
sums = np.sum(dice_rolls, axis=1)

# Create a histogram to visualize the distribution
plt.hist(sums, bins=range(num_dice, 6 * num_dice + 1), density=True, alpha=0.6, color='b')

plt.xlabel('Sum of Dice Rolls')
plt.ylabel('Probability Density')
plt.title('Sum of Three Dice Rolls (Gaussian Approximation)')
plt.legend()
plt.grid(True)
plt.show()


# Calculate the expected mean and standard deviation for the sum of three dice
# expected_mean = num_dice * (1 + 6) / 2
# expected_std_dev = np.sqrt(num_dice * (6**2 - 1) / 12)
# Plot a Gaussian distribution curve based on the expected mean and standard deviation
# x = np.linspace(num_dice, 6 * num_dice, 1000)
# gaussian_curve = 1 / (expected_std_dev * np.sqrt(2 * np.pi)) * np.exp(-(x - expected_mean)**2 / (2 * expected_std_dev**2))
# plt.plot(x, gaussian_curve, 'r', label='Gaussian Distribution')
