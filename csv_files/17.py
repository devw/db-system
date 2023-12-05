import numpy as np

# Example data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
z = [12, 11, 13, 2, 5]


print("Pearson Correlation Coefficient:",  np.corrcoef(x, z))
