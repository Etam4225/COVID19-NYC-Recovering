import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





#COVID became prevalant in 2020, appeared first in 2019


revenue_val = pd.read_csv("New_York_City_Tax_Revenue_Actuals.csv") #read csv file

revenue_val = revenue_val[revenue_val.FISCAL_YEAR > 2016] #only grab fiscal year > 2017


revenue_val['AMOUNT'] = revenue_val['AMOUNT'].str.replace(",", "")
revenue_val['AMOUNT'] = revenue_val['AMOUNT'].astype(int)

dfgp = revenue_val.groupby(['FISCAL_YEAR'])['AMOUNT'].mean()
print(dfgp)


# print(revenue_val.dtype)
dfgp.plot(kind='bar', title='NYC Annual (Actual) Mean Tax Revenue', ylabel='Mean Revenue per Year',
        xlabel='Year', figsize=(9, 8))
#revenue_val.groupby(['FISCAL_YEAR', 'TAX_NAME'])

#revenue_val['revenue_type_year'] = revenue_val['FISCAL_YEAR'] + '_' + revenue_val['AMOUNT']

# print(revenue_val)
#
#
#
# revenue_val.plot(kind = 'bar', x = 'FISCAL_YEAR', y = 'AMOUNT')

#revenue_val.plot()

plt.show()




#fig = (df_)
#fig.show()
# ax = revenue_val.plot.bar(x = 'FISCAL_YEAR',  y = 'AMOUNT', rot = 0)
#revenue_val.plot(x = 'FISCAL_YEAR', y = 'AMOUNT', kind = 'bar', figsize(9,8))
#plt.show()
