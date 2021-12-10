
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("laus_2_sheet1.csv")

df = df[df[' YEAR'] > 2016] #space in YEAR column

df.columns = df.columns.str.strip() #strip any spaces in columns which several do

df = df.loc[(df['AREA'] == 'Kings County') | (df['AREA'] == 'Bronx County') | (df['AREA'] == 'New York County') | (df['AREA'] == 'Richmond County') | (df['AREA'] == 'Queens County')] #get only the 5 counties in NYC

print(df.columns)

print(df)

dfgp = df.groupby(['AREA', 'YEAR'])['UNEMPRATE'].mean().reset_index() #Find the mean unemployment rate, grouping by the area and the year
print(dfgp)



p = sns.barplot(data = dfgp, x = 'AREA', y = 'UNEMPRATE', hue = 'YEAR') #sns barplot where we group by the AREA and color (hue) by year to show unemployment rate in the NYC counties

p.set(title = "Unemployment % Rate in NYC Counties in 2017-2021")

plt.show()
