import pandas as pd
file = pd.read_csv("C:/Users/my pc/Downloads/ecommerce_sales_analytics_5000.csv")
#using describe functon
print(file["revenue"].describe())
print(file["revenue"].skew())#positive skewed
print(file["revenue"].mean(),file["revenue"].median())#mean is write side of median so right skewed
#Inter quantile range:
Q1 = file["revenue"].quantile(0.25)
Q3 = file["revenue"].quantile(0.75)
IQR = Q3 -Q1
print(f"IQR: {IQR}")
print((Q3>Q1)and(IQR>0))
