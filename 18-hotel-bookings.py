import pandas as pd

df = pd.read_csv("csv_files/hotel_bookings.csv")


print(df["hotel"].unique())
