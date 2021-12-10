import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from pathlib import Path
from datetime import date
from pandas.tseries.offsets import MonthEnd



df = pd.read_csv("nyc_data.csv")

# print(df)

df = df.dropna() #drop any na rows.


df = df[df['YEAR'] >= 2017] #grab years 2017-2021
df['YEAR'] = df['YEAR'].astype(int) #parse as int

df['Unemployment Rate'] = df['Unemployment Rate'].astype(float) #set unemployment rate as a float for math calc later
df['Labor Force'] = df['Labor Force'].str.replace(",", "").astype(int) #clear any commas in our column

# print(df['Labor Force'])


# print(df.dtypes)


dfgp = df.groupby(['YEAR'])['Labor Force'].mean() #Find the labor force count and find the average of every year
print(dfgp)

dfgp1 = df.groupby(['YEAR']).mean()#Group by year again, but calculate the mean of the unemployment rate
print(dfgp1)


dfgp.plot(kind='bar', title='NYC Mean Labor Force By Year', ylabel='Mean labor force',  #plot mean labor force by year
        xlabel='year', figsize=(9, 8))

plt.ticklabel_format(style = 'plain', axis = 'y')


ax = dfgp.plot(kind='bar', title='NYC Mean Labor Force By Year / Mean Unemployment Rate (Line)', ylabel='Mean labor force',  #plot mean labor force by year
        xlabel='year', figsize=(9, 8), color = 'green')

ax2 = ax.twinx() #twin plot to use for our plot below

ax2.plot(dfgp1[['Unemployment Rate']].values,linestyle='-', marker='o', linewidth=2.5,color ='blue') #also plot the mean unemployment using a secondary y
ax2.set_ylabel("Mean Unemployment %")


plt.show()
