import pandas as pd
file = pd.read_csv("C:/Users/my pc/Downloads/ecommerce_sales_analytics_5000.csv")
numeric_file = file[["quantity","unit_price","discount","delivery_days","customer_rating","revenue"]]
print("\nCovariance:\n",numeric_file.cov())
print("Corelation:\n",numeric_file.corr()*100)
#focusing on revenue relationship
print((numeric_file.corr()*100)["revenue"].sort_values(ascending=False))
#Verification
print("Min=",(numeric_file.corr()*100).values.min())
print("Max=",(numeric_file.corr()*100).values.max())
