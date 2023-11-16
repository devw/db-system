import matplotlib.pyplot as plt
data = {
    'x': [1, 2, 2, 3, 4, 5, 6, 7, 9, 10],
    'y': [1, 2, 2, 3, 4, 5, 6, 7, 9, 10],
    'z': [2, 3, 4, 3, 3, 2, 3, 4, 8, 9]
}

# Create a figure and divide it into subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Plot the first graph (x and z)
axs[0].scatter(data['x'], data['z'], marker='*', linestyle='-', color='blue', label='X and Z')

# Plot the second graph (x and y)
axs[1].scatter(data['x'], data['y'], marker='o', linestyle='-', color='red', label='X and Y')

# Set labels for each subplot
# axs[0].set_xlabel('X-axis')
# axs[0].set_ylabel('Z-axis')
# axs[1].set_xlabel('X-axis')
# axs[1].set_ylabel('Y-axis')

# Add legends to each subplot
# axs[0].legend()
# axs[1].legend()

# Adjust layout
# plt.tight_layout()

# Show the combined plot
plt.show()
