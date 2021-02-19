import datetime as dt
import pandas_datareader.data as web
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('dark_background')


start = dt.datetime(2000, 1, 1)
now = dt.datetime.now()
ticker = input('enter a stock/etf ticker: ')
df = web.DataReader(ticker, 'yahoo', start, now)

df['Volitility'] = abs((df['Adj Close'] - df['Open']) / df['Open'])

x = df['Volatility']
y = df['Volume']

sns.jointplot(x='Volatility', y='Volume', data=df, color='red', kind='scatter')


plt.show()
