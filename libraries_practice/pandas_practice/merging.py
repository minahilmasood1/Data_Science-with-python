import pandas as pd            #joining and merging data frames
customers = pd.DataFrame({"Customer_id" :[1,2,3],"Name":["Alice","Bob","Charlie"]})
orders = pd.DataFrame({"Order_id":[101,102,103,],
                       "Customer_id":[1,2,2],
                       "Amount":[250,150,200]})
#Inner Merge
df_inner = pd.merge(customers,orders,on="Customer_id",how="inner")
print(f"Inner merge\n {df_inner}")
#Left merge
df_left = pd.merge(customers,orders,on="Customer_id",how="left")
print(f"left merge\n {df_left}")
df_right = pd.merge(customers,orders,on="Customer_id",how="right")
print(f"right merge\n {df_right}")
df_outer = pd.merge(customers,orders,on="Customer_id",how="outer")
print(f"outer merge\n {df_outer}")
#Concatinate dataframes
concate = pd.concat([customers,customers])
print(f"Concatenated rows:\n {concate}")
