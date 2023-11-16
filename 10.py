import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csv_files/insurance.csv")

df_smoker = df[df['smoker'] == 'yes']
df_no_smoker = df[df['smoker'] == 'no']

plt.scatter(df_smoker["bmi"], df_smoker["charges"], label="smoker")
plt.scatter(df_no_smoker["bmi"], df_no_smoker["charges"], label="no smoker")
plt.legend()
plt.show()
