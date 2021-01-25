# this is a properitary trading indicator that I developed
# it takes the derivative of a simple moving average, and
# then two moving averages of the given derivative. 
# this can be used to spot reversals. 

import sympy as sym
import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt

plt.style.use('dark_background')

ticker = 'qqq'
start = dt.datetime(2018, 5, 1)
end = dt.datetime.now()

df = web.DataReader(ticker, 'yahoo', start, end)

df['90sma'] = df['Adj Close'].rolling(window=20).mean()
df['20sma'] = df['Adj Close'].rolling(window=20).mean()
df['10sma'] = df['Adj Close'].rolling(window=10).mean()

class DataVisualization:

    def mpl(self):
        fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
        dv = ax[0]
        price = ax[1]

        df['90sma_derivative'] = sym.diff(df['90sma'])
        df['90sma_derivative_20sma'] = df['90sma_derivative'].rolling(window=13).mean()
        df['90sma_derivative_10sma'] = df['90sma_derivative'].rolling(window=5).mean()

        # dv.plot(df.index, df['90sma_derivative'], color='white', label="d/dx 90 sma")
        dv.plot(df.index, df['90sma_derivative_20sma'], color='red', label='20 sma')
        dv.plot(df.index, df['90sma_derivative_10sma'], color='green', label='10 sma')
        dv.set_title('Derivative Crossover & {} Chart'.format(ticker.upper()))
        dv.legend(loc='best')

        price.plot(df.index, df['Adj Close'])
        price.plot(df.index, df['20sma'])
        price.plot(df.index, df['10sma'])



        plt.show()

object = DataVisualization
object.mpl(DataVisualization)
