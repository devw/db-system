import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csv_files/stocks.csv")

aapl = df[df["symbol"] == "AAPL"]
x = aapl["date"]
y = aapl["price"]

msft = df[df["symbol"] == "MSFT"]
y2 = msft["price"]

plt.plot(x, y, label="Apple")
plt.plot(x, y2, label="Microsoft")
plt.xticks(x[::6], rotation=45)
plt.tight_layout()
plt.legend()

plt.show()
