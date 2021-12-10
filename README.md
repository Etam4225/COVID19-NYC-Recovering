## Is NYC recovering from COVID-19?

![NYC](https://www.topviewnyc.com/content/uploads/packages/5b6073e798d38_4_800.jpg)

## Overview:
This project is designed to analyze New York City's recovery from COVID-19 and to determine whether or not NYC is actually recovering. I take a loot at several datasets to prove or disprove the theory as shown below. For this project, I focused primarily on the business sector side to determine if NYC is recovering. I believe it is but slowly. As we all know COVID-19 was discovefred first in 2019 (hence COVID-19). So I looked at data around 2019 (more specifically in 2017-Present [Where Possible].

# Table of Contents:
- [Is NYC recovering from COVID-19?](#is-nyc-recovering-from-covid-19)
- [Overview:](#overview)
- [Tax Revenue of NYC during and before COVID-19](#tax-revenue-of-nyc-during-and-before-covid-19)
	- [Additional Note:](#additional-note)
- [Unemployment in NYC](#unemployment-in-nyc)
- [A look at unemployment in NY State](#a-look-at-unemployment-in-ny-state)
- [Further Analysis of Employment in NY (NYC Specifically)](#further-analysis-of-employment-in-ny-nyc-specifically)
- [Techniques](#techniques)
- [Conclusion](#conclusion)
- [Sources:](#sources)
- [END](#end)


## Tax Revenue of NYC during and before COVID-19

I gathered data that provided me details on the revenue NYC earned during previous years, including when COVID-19 hit. As you all know, Hunter College closed it's doors at around March 2020 and there was a 2 week lockdown imposed on many citizens. As such, for 2020's tax revenue I expected to see quite a decrease in revenue. However, the data I've gathered shows otherwise.

Below is a graph of the mean actual NYC tax revenue annually (**In millions of dollars**). (This graph is the combined results of various sectors of tax revenue which includes various taxes like cigarette tax, real property tax, commerical rent tax, business corp tax, etc.)

![Mean Actual NYC Tax Revenue by Year](https://raw.githubusercontent.com/Etam4225/COVID19-NYC-Recovering/main/Mean%20annual%20Revenue%20Yearly.PNG)

| FISCAL_YEAR  | Mean Actual Tax Revenue |
| ------------- | ------------- |
| 2017  | 3644.133333  |
| 2018  | 3940.666667  |
| 2019  | 4392.285714  |
|2020   | 4506.357143  |

One thing to note is the difference in Mean Actual Tax Revenue between each year. We'll notice that the gain in tax revenue is lowest between 2019 and 2020 (a difference of 114.071429). So, it's evidently clear that COVID-19 **DID** have an effect in 2020 where tax revenue had declined about 300 million dollars (compared to 2018-2019) where it trended downward in 2020. So, in 2020 COVID-19 had a significant, negative effect on economy in NYC.

### Additional Note:
Unfortunately, 2021's revenue data is not available (the year still isn't complete) and I have yet to find data for it either.

Despite that, I do suspsect revenue on 2021 to nonetheless be lower, I think after the project ends, I could still update the bar graph to reflect this. If it indeed is HIGHER than 2020, I think that'd be an interesting point to point out that NYC is recovering albeit very slowly, however, as I stated earlier, my prediction for 2021 is that tax revenue has gone down or is close to the revenue of 2020 - I would of course like to have that data if possible.

Looking at unemployment, however, does tell as a more interesting, revealing story.

## Unemployment in NYC

![Unemployment Rates by Year (2017-2021)](https://raw.githubusercontent.com/Etam4225/COVID19-NYC-Recovering/main/Figure_1.png)

(NOT Seasonally Adjusted)

We can see that in 2017-2019, unemployment rates are relatively close and unchanged. Then, we see a massive jump (yes, this is what actually happened) from March and up in 2020.
The change jumped from 4.20% to 15.20% an 11% jump. The following months, the rate stayed fairly high. Then going into 2021, we can see a relative trend that unemployment rates are indeed going down to suggest, NYC is slowly recovering from the effects, at least economy-wise.

## A look at unemployment in NY State
![Unemployment Rates in Octobe 2021](https://raw.githubusercontent.com/Etam4225/COVID19-NYC-Recovering/main/Department%20of%20Labor%20New%20York%20unemployment%20rate.PNG)

Source: [New York Department of Labor](https://dol.ny.gov/system/files/documents/2021/11/state-labor-department-releases-preliminary-october-2021-area-unemployment-rates.pdf)

This takes a look at NY overall which points out in general that NYC is doing worse objectively compared to New York's other counties.

## Further Analysis of Employment in NY (NYC Specifically)
(Seasonally Adjusted data used here)

Here, I looked at the workforce of NYC as the dataframe provides the following data:

| YEAR  | Mean of Labor Force |
| ------------- | ------------- |
|2017  |  4,116,740|
|2018 |   4,075,573|
|2019  |  4,071,296|
|2020  |  3,908,636|
|2021  |  4,007,027|

And the graph below:

![NYC's Mean Labor Force](https://raw.githubusercontent.com/Etam4225/COVID19-NYC-Recovering/main/Mean%20annual%20Revenue%20Yearly.PNG)

The data shows that the labor force dropped slightly going into 2020 when covid hit, despite that, the labor force seems roughly the same from each year in 2017-2021. WE also see that the labor force bounced back slightly from 2020 to 2021.

I also used the same graph except I graphed it alongside the unemployment rate which tells us some additional interesting info:


 | YEAR  | Unemployment % |
| ------------- | ------------- |
|2017 | 4.525000|
|2018   | 4.116667|
|2019   |   3.858333|
|2020    |  12.458333|
|2021    |  11.000000|

![NYC's Mean Labor Force / Graphed with Unemployment rate (as a Line plot)](https://raw.githubusercontent.com/Etam4225/COVID19-NYC-Recovering/main/Mean%20Labor%20Force%20and%20Mean%20unemployment.PNG)

Looking at this data, we can see that after covid hit in 2019, it had a huge impact on unemployment rate, even though the labor force dropped only slightly. In fact, doing the math, unemployed ROSE by nearly 4 times the amount from 2019 to 2020. Clearly in 2021, the data shows we are recovering again, but very slowly and nowhere near back to the 3-4% unemployment rate we saw back in 2019 and 2018



## Techniques
I used several libraries to create the graphs shown on the website. The libraries I used included: pandas, matplotlib, seaborn, and numpy. These libraries were critical in the development of my graphs as they were invaluable in providing useful and intriguing visualizations that could help to better explain the situation with COVID-19 and New York. I also used one graph from the Department of Labor from their page to help us look at the overal picture in New York State.

## Conclusion

Although analyzing tax revenue gave me inconclusive data, from taking a look at unemployment data, I was able to see that NYC was recovering somewhat from the big fall in 2020 going into 2021. I am however, genuinely curious what the data will show for the 2021 tax revenue because I wonder if it'd show a similar story as with looking at unemployment or not. Nonetheless, there is still some evidence showing that NYC is recovering, but certainly at a slow rate and has not totally recovered by any means from the impact of COVID-19 (which we still see today).

# Sources:
[Cases of Covid](https://data.cityofnewyork.us/Health/COVID-19-Daily-Counts-of-Cases-Hospitalizations-an/rc75-m7u3/data)  
[Actual Tax Revenue](https://data.cityofnewyork.us/City-Government/New-York-City-Tax-Revenue-Actuals/j3uq-sh95)  
[Unemployment Rates](https://statistics.labor.ny.gov/laus.asp)  
[New York Department of Labor](https://dol.ny.gov/system/files/documents/2021/11/state-labor-department-releases-preliminary-october-2021-area-unemployment-rates.pdf)

[Stack Overflow resource for restricting scientific notifcation](https://stackoverflow.com/questions/46735745/how-to-control-scientific-notation-in-matplotlib)

# END

