import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv("csv_files/airbnb-prices/paris_weekdays.csv")

# Assuming you have a dataset with cleanliness_rating, metro_dist, and realSum columns
# X is the matrix of independent variables, and y is the vector of the dependent variable
metro_dist_h =df [ df["metro_dist"] > 2] 
metro_dist_l = df [ df["metro_dist"] <= 2]

print(metro_dist_h)

realSum_h = metro_dist_h["realSum"]
realSum_l = metro_dist_l["realSum"]

# # Plot the actual vs predicted values
plt.boxplot([realSum_h, realSum_l], labels=["> 2", "<= 2"])
plt.show()
