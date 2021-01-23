import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader as web
import datetime as dt
from sklearn import metrics
plt.style.use('dark_background')

class Trading():

    def algo(self):
        # loaded data
        ticker = input('enter a stock ticker')
        start = dt.datetime(2000, 1, 1)
        end = dt.datetime.now()

        df = web.DataReader(ticker, 'yahoo', start, end)

        def LRegression():
            # X & y
            # X = features
            # y = predictions
            X = df[['High', 'Low', 'Open', 'Volume']]
            y = df['Adj Close']

            # TTS (splitting data)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

            # creating LinearRegression Object
            lm = LinearRegression()

            # train/fit data
            lm.fit(X_train, y_train)

            # assign predictions
            predictions = lm.predict(X_test)

            # variable assignment for scatter plot
            x, y = y_test, predictions
            plt.scatter(x, y, color='white', label='points', edgecolors='red')

            # line of best fit
            m, b = np.polyfit(x, y, 1)
            plt.plot(x, m * x + b, label='Line of Best fit', color='purple')

            # metrics
            MAE = metrics.mean_absolute_error(y_test, predictions).__round__(2)
            MSE = metrics.mean_squared_error(y_test, predictions).__round__(2)
            RMSE = np.sqrt(metrics.mean_squared_error(y_test, predictions)).round(2)

            print('MAE: ', MAE)
            print('MSE: ', MSE)
            print('RMSE: ', RMSE)

            # plotting stuff
            plt.xlabel('y_test')
            plt.plot()
            plt.ylabel('Predictions')
            plt.legend(loc='best')
            plt.show()

        LRegression()

a = Trading()
a.algo()
print('done')