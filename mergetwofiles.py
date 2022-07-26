import pandas as pd

data1= pd.read_csv("Scores_Subset.csv")

data2=pd.read_csv("Index_Subset.csv")

output = pd.merge(data1, data2, on='date',how='right')

output.to_csv('raw_data1.csv', index=False)
