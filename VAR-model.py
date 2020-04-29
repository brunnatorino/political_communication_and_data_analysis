from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
from statsmodels.tools.eval_measures import rmse, aic

economy['TIME'] = economy.index
rates['TIME'] = rates.index
unemployment['TIME'] = unemployment.index
wages['TIME'] = wages.index
inflation['TIME'] = inflation.index
trade['TIME'] = trade.index
recession['TIME'] = recession.index
everything['TIME'] = everything.index

economy['TIME'] = pd.to_datetime(economy['TIME'],format='%d%m%Y')
economy.loc[economy["TIME"] != 1,'First_Day'] = economy['TIME'] + pd.offsets.MonthBegin(1)
economy['year'], economy['month'], economy['day'] = economy['First_Day'].dt.year, economy['First_Day'].dt.month,economy['First_Day'].dt.day

rates['TIME'] = pd.to_datetime(rates['TIME'],format='%d%m%Y')
rates.loc[rates["TIME"] != 1,'First_Day'] = rates['TIME'] + pd.offsets.MonthBegin(1)
rates['year'], rates['month'], rates['day'] = rates['First_Day'].dt.year, rates['First_Day'].dt.month,rates['First_Day'].dt.day

unemployment['TIME'] = pd.to_datetime(unemployment['TIME'],format='%d%m%Y')
unemployment.loc[unemployment["TIME"] != 1,'First_Day'] = unemployment['TIME'] + pd.offsets.MonthBegin(1)
unemployment['year'], unemployment['month'], unemployment['day'] = unemployment['First_Day'].dt.year, unemployment['First_Day'].dt.month,unemployment['First_Day'].dt.day

wages['TIME'] = pd.to_datetime(wages['TIME'],format='%d%m%Y')
wages.loc[wages["TIME"] != 1,'First_Day'] = wages['TIME'] + pd.offsets.MonthBegin(1)
wages['year'], wages['month'], wages['day'] = wages['First_Day'].dt.year, wages['First_Day'].dt.month,wages['First_Day'].dt.day

inflation['TIME'] = pd.to_datetime(inflation['TIME'],format='%d%m%Y')
inflation.loc[inflation["TIME"] != 1,'First_Day'] = inflation['TIME'] + pd.offsets.MonthBegin(1)
inflation['year'], inflation['month'], inflation['day'] = inflation['First_Day'].dt.year, inflation['First_Day'].dt.month,inflation['First_Day'].dt.day

trade['TIME'] = pd.to_datetime(trade['TIME'],format='%d%m%Y')
trade.loc[trade["TIME"] != 1,'First_Day'] = trade['TIME'] + pd.offsets.MonthBegin(1)
trade['year'], trade['month'], trade['day'] = trade['First_Day'].dt.year, trade['First_Day'].dt.month,trade['First_Day'].dt.day

recession['TIME'] = pd.to_datetime(recession['TIME'],format='%d%m%Y')
recession.loc[recession["TIME"] != 1,'First_Day'] = recession['TIME'] + pd.offsets.MonthBegin(1)
recession['year'], recession['month'], recession['day'] = recession['First_Day'].dt.year, recession['First_Day'].dt.month,recession['First_Day'].dt.day

everything['TIME'] = pd.to_datetime(everything['TIME'],format='%d%m%Y')
everything.loc[everything["TIME"] != 1,'First_Day'] = everything['TIME'] + pd.offsets.MonthBegin(1)
everything['year'], everything['month'], everything['day'] = everything['First_Day'].dt.year, everything['First_Day'].dt.month,everything['First_Day'].dt.day

economy['key'] = economy['year'].astype(str) + economy['month'].astype(str)
rates['key'] = rates['year'].astype(str) + rates['month'].astype(str)
unemployment['key'] = unemployment['year'].astype(str) + unemployment['month'].astype(str)
wages['key'] = wages['year'].astype(str) + wages['month'].astype(str)
inflation['key'] = inflation['year'].astype(str) + inflation['month'].astype(str)
trade['key'] = trade['year'].astype(str) + trade['month'].astype(str)
recession['key'] = recession['year'].astype(str) + recession['month'].astype(str)
everything['key'] = everything['year'].astype(str) + everything['month'].astype(str)

economy = economy['2014-1-1':'2017-4-1']
rates = rates['2014-1-1':'2017-4-1']
unemployment = unemployment['2014-1-1':'2017-4-1']
wages = wages['2014-1-1':'2017-4-1']
inflation = inflation['2014-1-1':'2017-4-1']
trade = trade['2014-1-1':'2017-4-1']
recession = recession['2014-1-1':'2017-4-1']
everything = everything['2014-1-1':'2017-4-1']

df_mean = economy.groupby(['key']).polarity.sum()
s = df_mean.to_dict()
economy['polarity_grouped'] = economy.key.replace(s)

df_mean = rates.groupby(['key']).polarity.sum()
s = df_mean.to_dict()
rates['polarity_grouped'] = rates.key.replace(s)

df_mean = unemployment.groupby(['key']).polarity.sum()
s = df_mean.to_dict()
unemployment['polarity_grouped'] = unemployment.key.replace(s)

df_mean = wages.groupby(['key']).polarity.sum()
s = df_mean.to_dict()
wages['polarity_grouped'] = wages.key.replace(s)

df_mean = inflation.groupby(['key']).polarity.sum()
s = df_mean.to_dict()
inflation['polarity_grouped'] = inflation.key.replace(s)

df_mean = trade.groupby(['key']).polarity.sum()
s = df_mean.to_dict()
trade['polarity_grouped'] = trade.key.replace(s)

df_mean = recession.groupby(['key']).polarity.sum()
s = df_mean.to_dict()
recession['polarity_grouped'] = recession.key.replace(s)

df_mean = everything.groupby(['key']).polarity.sum()
s = df_mean.to_dict()
everything['polarity_grouped'] = everything.key.replace(s)

df_mean = economy.groupby(['key']).polarity_title.sum()
s = df_mean.to_dict()
economy['polarity_title_grouped'] = economy.key.replace(s)

df_mean = rates.groupby(['key']).polarity_title.sum()
s = df_mean.to_dict()
rates['polarity_title_grouped'] = rates.key.replace(s)

df_mean = unemployment.groupby(['key']).polarity_title.sum()
s = df_mean.to_dict()
unemployment['polarity_title_grouped'] = unemployment.key.replace(s)

df_mean = wages.groupby(['key']).polarity_title.sum()
s = df_mean.to_dict()
wages['polarity_title_grouped'] = wages.key.replace(s)

df_mean = inflation.groupby(['key']).polarity_title.sum()
s = df_mean.to_dict()
inflation['polarity_title_grouped'] = inflation.key.replace(s)

df_mean = trade.groupby(['key']).polarity_title.sum()
s = df_mean.to_dict()
trade['polarity_title_grouped'] = trade.key.replace(s)

df_mean = recession.groupby(['key']).polarity_title.sum()
s = df_mean.to_dict()
recession['polarity_title_grouped'] = recession.key.replace(s)

df_mean = recession.groupby(['key']).polarity_title.sum()
s = df_mean.to_dict()
everything['polarity_title_grouped'] = everything.key.replace(s)


USA['year'], USA['month'] = USA['TIME'].dt.year, USA['TIME'].dt.month
USA['key'] = USA['year'].astype(str) + USA['month'].astype(str)
mapping = USA.set_index('key').to_dict()['Value']

everything['Value'] = everything['key'].replace(mapping)
economy['Value'] = economy['key'].replace(mapping)
rates['Value'] = rates['key'].replace(mapping)
unemployment['Value'] = unemployment['key'].replace(mapping)
wages['Value'] = wages['key'].replace(mapping)
inflation['Value'] = inflation['key'].replace(mapping)
trade['Value'] = trade['key'].replace(mapping)
recession['Value'] = recession['key'].replace(mapping)

economy['polarity_grouped'] = economy['polarity_grouped']*100
economy['polarity_title_grouped'] = economy['polarity_title_grouped']*100

inflation['polarity_grouped'] = inflation['polarity_grouped']*100
inflation['polarity_title_grouped'] = inflation['polarity_title_grouped']*100

wages['polarity_grouped'] = wages['polarity_grouped']*100
wages['polarity_title_grouped'] = wages['polarity_title_grouped']*100

unemployment['polarity_grouped'] = unemployment['polarity_grouped']*100
unemployment['polarity_title_grouped'] = unemployment['polarity_title_grouped']*100

rates['polarity_grouped'] = rates['polarity_grouped']*100
rates['polarity_title_grouped'] = rates['polarity_title_grouped']*100

trade['polarity_grouped'] = trade['polarity_grouped']*100
trade['polarity_title_grouped'] = trade['polarity_title_grouped']*100

recession['polarity_grouped'] = recession['polarity_grouped']*100
recession['polarity_title_grouped'] = recession['polarity_title_grouped']*100

everything['polarity_grouped'] = everything['polarity_grouped']*100
everything['polarity_title_grouped'] = everything['polarity_title_grouped']*100
import seaborn as sns 

sns.set(style="darkgrid")
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
sns.set(rc={'figure.figsize':(11.7,8.27)})


# Plot the responses for different events and regions
sns.lineplot(x=wages.index, y="polarity_grouped",data=wages)

import seaborn as sns 

sns.set(style="darkgrid")
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
sns.set(rc={'figure.figsize':(11.7,8.27)})


# Plot the responses for different events and regions
sns.lineplot(x=USA.index, y="Value",data=USA)

import numpy as np
import pandas
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
economy.to_excel('economy.xlsx')
rates.to_excel('rates.xlsx')
unemployment.to_excel('unemployment.xlsx')
inflation.to_excel('inflation.xlsx')
wages.to_excel('wages.xlsx')
trade.to_excel('trade.xlsx')
recession.to_excel('recession.xlsx')
data = economy[['polarity_grouped','polarity_title_grouped','Value']]
model = VAR(data)
results = model.fit(ic='bic')
results.summary()


data1 = rates[['polarity_grouped','polarity_title_grouped','Value']]
model = VAR(data1)
results1 = model.fit(ic='bic')
results1.summary()

data2 = unemployment[['polarity_grouped','polarity_title_grouped','Value']]
model = VAR(data2)
results2 = model.fit(ic='bic')
results2.summary()

data3 = trade[['polarity_grouped','polarity_title_grouped','Value']]
model = VAR(data3)
results3 = model.fit(ic='bic')
results3.summary()

data4 = inflation[['polarity_grouped','polarity_title_grouped','Value']]
model = VAR(data4)
results4 = model.fit(ic='bic')
results4.summary()

data5 = wages[['polarity_grouped','polarity_title_grouped','Value']]
model = VAR(data5)
results5 = model.fit(ic='bic')
results5.summary()

data6 = recession[['polarity_grouped','polarity_title_grouped','Value']]
model = VAR(data6)
results6 = model.fit(ic='bic')
results6.summary()

data7 = everything[['polarity_grouped','polarity_title_grouped','Value']]
model = VAR(data7)
results7 = model.fit(ic='bic')
results7.summary()


print(results.test_causality('Value', ['polarity_grouped', 'polarity_title_grouped'], kind='f'))
print(results1.test_causality('Value', ['polarity_grouped', 'polarity_title_grouped'], kind='f'))
print(results2.test_causality('Value', ['polarity_grouped', 'polarity_title_grouped'], kind='f'))
print(results3.test_causality('Value', ['polarity_grouped', 'polarity_title_grouped'], kind='f'))
print(results4.test_causality('Value', ['polarity_grouped', 'polarity_title_grouped'], kind='f'))
print(results5.test_causality('Value', ['polarity_grouped', 'polarity_title_grouped'], kind='f'))
print(results6.test_causality('Value', ['polarity_grouped', 'polarity_title_grouped'], kind='f'))
print(results7.test_causality('Value', ['polarity_grouped', 'polarity_title_grouped'], kind='f'))

results5.plot()

results1.plot_forecast(10)

irf = results.irf(3)
irf.plot(orth=True)
