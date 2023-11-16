import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset with three columns (x, y, and yes/no)
# data = [
#     (1, 2, "yes"),
#     (2, 3, "no"),
#     (3, 1, "yes"),
#     (4, 4, "no"),
#     (5, 2, "yes"),
#     (6, 3, "no"),
#     (7, 1, "yes"),
# ]

# Separate data into 'yes' and 'no' categories
# x_yes = [row[0] for row in data if row[2] == "yes"]
# y_yes = [row[1] for row in data if row[2] == "yes"]
# x_no = [row[0] for row in data if row[2] == "no"]
# y_no = [row[1] for row in data if row[2] == "no"]

# Create a scatter plot with different colors for 'yes' and 'no'
# plt.scatter(x_yes, y_yes, color='green', label='Yes')
# plt.scatter(x_no, y_no, color='red', label='No')

# Set labels and legend
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()

# Show the plot
# plt.show()
# Create a DataFrame from your data



# data = {
#     'x': [x for x in range(10)],
#     'y1': [x + 1 for x in range(10)],
#     'y2': [x - 1 for x in range(10)],
# 	'y3': [x + 2 for x in range(10)]
# }
# df = pd.DataFrame(data)
# plt.scatter(data['x'], data['y1'], label="y1")
# plt.scatter(df['x'], df['y2'])
# plt.scatter(df['x'], df['y3'])
# plt.legend()
# plt.show()


data = {
    'x': [1, 2, 2, 3, 4, 1, 2, 3, 4],
    'y': [1, 2, 2, 3, 4, 5, 4, 2, 2],
    'z': ['yes', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no',]
}
df = pd.DataFrame(data)
# Separate data into 'yes' and 'no' categories
print(df)
yes_data = df[df['z'] == 'yes']
print(yes_data)
no_data = df[df['z'] == 'no']
print(no_data)

# Create a scatter plot with different colors for 'yes' and 'no'
plt.scatter(yes_data['x'], yes_data['y'], color='#0fff0f', label='Yes')
plt.scatter(no_data['x'], no_data['y'], color='#ff0000', label='No')

# Set labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show the plot
plt.show()
