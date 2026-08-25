import pandas as pd
#Dataframes are 2D,consist of rows and columns in tabular form
data = {"Name":"Ali","Class":4,"Subject": "English","School":"FG","CIty":"Islamabad"}
d = pd.DataFrame(data,index=[1])
print(d)
file = pd.read_csv("C:/Users/my pc/Downloads/retail_sales.csv") #loadinf file into pd dataframe
#Some common methods and attributes:
file.info()
print(file.describe())
print(file.shape)
print(file.value_counts())
print(file.size)
#Labelled based selection
s = d.loc[0:1,"Name":"School"]
print(s)
#Index based selection
i = d.iloc[0:1,2:4]
print(i)
#Attribute based selection(Boolean filtering)
a = file[file["Category"] == "Electronics"]
print(a)
#Assignment using loc:
d.loc[d["Name"]=="Ali","Class"]= 5
print(d.loc[d["Name"]=="Ali","Class"])
