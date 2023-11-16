import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csv_files/stocks.csv")
print(df)

aapl = df[df["symbol"] == "AAPL"]
print(aapl)
x = aapl["date"]
y = aapl["price"]

plt.plot(x, y)
plt.xticks(x[::6],  rotation='vertical')
plt.show()


