"""
Name: Ethan Tam
Email: ethan.tam33@myhunter.cuny.edu
Title: NYC Revenue in Relation to COVID-19 – Is NYC Recovering?
Resources: https://seaborn.pydata.org/generated/seaborn.lineplot.html, geeksforgeeks.org, https://data.cityofnewyork.us/Health/COVID-19-Daily-Counts-of-Cases-Hospitalizations-an/rc75-m7u3/data, https://data.cityofnewyork.us/City-Government/Revenue-Actuals/qbvv-9nzz/data
, https://data.cityofnewyork.us/City-Government/New-York-City-Tax-Revenue-Actuals/j3uq-sh95, https://dol.ny.gov/system/files/documents/2021/11/state-labor-department-releases-preliminary-october-2021-area-unemployment-rates.pdf, https://statistics.labor.ny.gov/lslaus.shtm

All CSVs used can be found in the github link: https://github.com/Etam4225/COVID19-NYC-Recovering
(I had filtered out some data manually onto new csvs to then read on the python file below. All Standalone py files can also be found on github. One was uploaded to github but was excluded in the overall project so was not included here.)


URL: https://github.com/Etam4225/COVID19-NYC-Recovering

COVID became prevalant in 2020, appeared first in 2019, Focused on data provided in 2017-Present (where possible)

Note: Left prints on the file for test code to see what dataframe looks like.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from pathlib import Path
from datetime import date
from pandas.tseries.offsets import MonthEnd

"""
Mean Labor Force/Unemployment Graph
"""

############################################################
def unemployment_bar():
    df = pd.read_csv("nyc_data.csv")

    # print(df)

    df = df.dropna() #drop any na rows.


    df = df[df['YEAR'] >= 2017] #grab years 2017-2021
    df['YEAR'] = df['YEAR'].astype(int) #parse as int

    df['Unemployment Rate'] = df['Unemployment Rate'].astype(float) #set unemployment rate as a float for math calc later
    df['Labor Force'] = df['Labor Force'].str.replace(",", "").astype(int) #clear any commas in our column


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
###########################################################


"""
Revenue Actual Graph
"""

###########################################################
def revenue_bar():
    revenue_val = pd.read_csv("New_York_City_Tax_Revenue_Actuals.csv") #read csv file

    revenue_val = revenue_val[revenue_val.FISCAL_YEAR > 2016] #only grab fiscal year > 2017


    revenue_val['AMOUNT'] = revenue_val['AMOUNT'].str.replace(",", "") #clear any commas
    revenue_val['AMOUNT'] = revenue_val['AMOUNT'].astype(int) #change the amount as an int to calculate values

    dfgp = revenue_val.groupby(['FISCAL_YEAR'])['AMOUNT'].mean() #group data by the fiscal amount
    print(dfgp)


    dfgp.plot(kind='bar', title='NYC Annual (Actual) Mean Tax Revenue', ylabel='Mean Revenue per Year',  #plot
            xlabel='Year', figsize=(9, 8))

    plt.show() #show plot
###########################################################


"""
Unemployment line graph throughout 2017-Present
"""
###########################################################
def unemployment_lineplot():

    #Before csv was read, I cleaned up the sheets and converted it into a single csv file with the unemployment info
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

    Unemployment_wide = Unemployment_wide.reindex(order, axis=0) #reindex our data
    p = sns.lineplot(data = Unemployment_wide) #plot our data
    p.set_ylabel("Unemployment Rate (Out of 1.00)")
    p.set(title = "Unemployment Rates in the Years 2017 - 2021")
    plt.show()
###########################################################


"""
Unemployment rate by county each year 2017-2021
"""
###########################################################
def unemployment_rate_by_county():
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
###########################################################

#function calls
unemployment_bar()
revenue_bar()
unemployment_lineplot()
unemployment_rate_by_county()
