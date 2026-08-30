import pandas as pd
file = pd.read_csv("ecommerce_sales_analytics_5000.csv")
#using map() function on a file
file["payment_type"] = file["payment_method"].map({"Wallet":"Digital",
                                                   "Card":"Digital",
                                                   "COD":"Cash"})
#Verification:
print(file["payment_type"].unique())                  #1
print(file[["payment_type","payment_method"]].head()) #2
print(file.groupby("payment_type").size())            #3
#Using apply() function
def revenue_category(rows):
    if rows["revenue"] > 500:
        return "High"
    elif rows["revenue"] >= 200:
        return "Medium"
    else:
        return "Low"
file["revenue_cat"] = file.apply(revenue_category,axis=1)
#Verification:
print(file["revenue_cat"].value_counts())
#Pipe() function:
def add_profit(data):
    data["profit"] = data["revenue"] * 0.20
    return data
def net_revenue(data):
    data["net_revenue"] = data["revenue"] - data["profit"]
    return data
file = file.pipe(add_profit).pipe(net_revenue)
#Verification:
print(file[["net_revenue", "revenue", "profit"]].sample(10))

