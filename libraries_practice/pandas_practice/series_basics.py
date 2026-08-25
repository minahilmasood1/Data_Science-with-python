import pandas as pd
#series = 1D arrays and building block of dataframes
s =  pd.Series([1,2,3,4,5,6,],index= ["a","b","c","d","e","f"])
print(s.values)
print(s.index)
s.value_counts()
