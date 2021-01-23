# this code can be used to determine the validity
# of a linear regression model when tested on
# the same data set

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader as web
import datetime as dt
plt.style.use('dark_background')

# loaded data
ticker = input('enter a stock ticker')
start = dt.datetime(2000, 1, 1)
end = dt.datetime.now()

df = web.DataReader(ticker, 'yahoo', start, end)


# X & y
X = df[['High', 'Low', 'Open', 'Volume']]
y = df['Adj Close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

lm = LinearRegression()

lm.fit(X_train, y_train)

p = lm.predict(X_test)
x, y = y_test, p



sns.distplot((y-x))

plt.show()



