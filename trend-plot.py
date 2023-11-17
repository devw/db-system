import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csv_files/stocks.csv")

aapl = df[df["symbol"] == "AAPL"]
x = aapl["date"]
y = aapl["price"]

msft = df[df["symbol"] == "MSFT"]
x2 = msft["date"]
y2 = msft["price"]

plt.plot(x, y)
plt.plot(x2, y2)
plt.xticks(x[::6], rotation=45)
plt.tight_layout()

plt.show()
