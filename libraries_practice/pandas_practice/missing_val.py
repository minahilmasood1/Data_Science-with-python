import pandas as pd
file = pd.read_csv("C:/Users/my pc/Downloads/retail_sales.csv",dtype={"Category":"category"})
print(file.isna().sum())
file["Quantity"]= pd.to_numeric(file["Quantity"])
file["Quantity"]= file["Quantity"].fillna(file["Quantity"].mode()[0])
file["Category"] = file["Category"].fillna(file["Category"].mode()[0])
file["Sales"] = file["Sales"].fillna(file["Sales"].median)
file["Profit"] = file["Profit"].dropna
file.dropna(subset=["Region"],inplace=True)
print(file.isna().sum())
file.info()
