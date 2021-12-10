"""
Unused dataset added into github for consistency
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




df = pd.read_csv("COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv") #read csv file


df['DATE_OF_INTEREST']=pd.to_datetime(df['DATE_OF_INTEREST'],format='%m/%d/%Y') #change the type of date into a dt format

# dfgp = df.groupby(df['DATE_OF_INTEREST'].dt.strftime('%B'))['CASE_COUNT'].sum().sort_values()

dfgp = df.groupby([df['DATE_OF_INTEREST'].dt.year.rename('year'),  #Group by YEAR AND MONTH - Stackoverflow help found: https://stackoverflow.com/questions/61879166/pandas-groupby-month-and-year-date-as-datetime64ns-and-summarized-by-count
df['DATE_OF_INTEREST'].dt.month_name().rename('Month')])['CASE_COUNT'].sum().reset_index()


Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


dfgp['Month'] = pd.Categorical(dfgp['Month'], categories = Months, ordered = True)
#
#
# dfgp.sort_values("Month")

print(dfgp.dtypes)

print(dfgp)
