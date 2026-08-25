import pandas as pd
file = pd.read_csv("retail_sales.csv",dtype={"Category":"category"})

#converting col. into date/time format
file["Date"] = pd.to_datetime(file["Date"],format=("mixed"),errors="coerce") #Library level utitlity function

#declaring col. into category after reading data
file["Region"] = file["Region"].astype("category") #instance method
file.info()
