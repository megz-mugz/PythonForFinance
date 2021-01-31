import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import random

class Linear_Regression:

    @staticmethod
    def random_data(user_num):

        array_one = []
        array_two = []
        for i in range(0, 1001):
            num1 = random.randint(0, 1001)
            if num1 < 333:
                num2 = random.randint(0, 333)
            elif num1 > 334 and num1 < 666:
                num2 = random.randint(334, 666)
            else:
                num2 = random.randint(666, 1001)

            array_one.append(num1)
            array_two.append(num2)

        arr1 = np.array(array_one).reshape(-1, 1)
        arr2 = np.array(array_two).reshape(-1, 1)

        X_train, X_test, y_train, y_test = train_test_split(arr1, arr2, test_size=0.4)

        model = LinearRegression()

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        print("Model Score:", ((model.score(X_test, y_test)) * 100).__round__(2))
        print('Mean Absolute Error:', mean_absolute_error(y_test, predictions))
        print('Mean Sqaured Error:', mean_squared_error(y_test, predictions))
        print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, predictions)))
        print(model.predict(np.array(user_num).reshape(-1, 1)))

        fig, ax = plt.subplots(nrows=1, ncols=2)

        train_data = ax[0]
        test_predict = ax[1]

        test_predict.set_title('Test vs Prediction Points')
        test_predict.set_xlabel('Test Data')
        test_predict.set_ylabel('Predicted Data')
        test_predict.scatter(y_test, predictions)
        test_predict.set_ylim(0, 1001)

        train_data.set_title('Training Data w/ Prediction Line')
        train_data.set_xlabel('X_train Data')
        train_data.set_ylabel('y_train Data')
        train_data.scatter(X_train, y_train)


        train_data.plot(np.linspace(0, 1001, 100).reshape(-1, 1), model.predict(np.linspace(0, 1001, 100).reshape(-1, 1)),
                        color='red')

        plt.show()


X = Linear_Regression
X.random_data(int(input('enter a number:')))