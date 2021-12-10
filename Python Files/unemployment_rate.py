import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from pathlib import Path
from datetime import date
from pandas.tseries.offsets import MonthEnd




#COVID became prevalant in 2020, appeared first in 2019


df = pd.read_csv("Unemployment Rates.csv")

# Unemployment['Date'] = pd.to_datetime(Unemployment[['Year', 'Month']].assign(DAY = 1))


df = df[['Year', 'Month', 'Rate']]
# Unemployment['Rate'] = Unemployment['Rate'].str.replace('%', '')
# Unemployment = Unemployment.drop('Ann Avg', axis = 1) #drop avg column

# years = mdates.YearLocator()   # every year
# months = mdates.MonthLocator()  # every month

df['Month'] = df['Month'].astype('category')

Months = ["Jan", "Feb", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

df['Month'] = pd.Categorical(df['Month'], categories = Months, ordered = True)

df['Rate'] = df['Rate'].str.rstrip('%').astype('float') / 100.0

print(df['Month'])


print(df.dtypes)

# fig, axes = plt.subplots()

order = df['Month']

Unemployment_wide = df.pivot_table(index = 'Month', columns = 'Year', values = 'Rate')

print(Unemployment_wide)

print(Unemployment_wide.dtypes)

Unemployment_wide = Unemployment_wide.reindex(order, axis=0)

# flights = sns.load_dataset('flights')
#
# flights_wide = flights.pivot_table(index='month', columns = 'year')
#
#
# # sns.lineplot(data = flights_wide)
# print(flights.dtypes)
#
# print(flights_wide)
p = sns.lineplot(data = Unemployment_wide)

p.set_ylabel("Unemployment Rate (Out of 1.00)")

p.set(title = "Unemployment Rates in the Years 2017 - 2021")
#
plt.show()
#
