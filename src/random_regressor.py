from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib
import numpy as np


"""
    MODEL: Random forest regression

"""


def train(x_train, y_train, filename):
    model = RandomForestRegressor(n_estimators=3)
    model.fit(x_train, y_train)

    print 'writing results to: %s' % filename
    joblib.dump(model, filename)


def test(filename, x_test, y_test):
    model = joblib.load(filename)
    y_predict = model.predict(x_test)
    print np.ravel(y_test)
    print np.ravel(y_predict)
    # The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_predict))
    # Explained variance score: 1 is perfect prediction
    print 'Variance score: %.2f' % r2_score(y_test, y_predict)


def predict(filename, x_test):
    model = joblib.load(filename)
    y_predict = model.predict(x_test)
    return np.ravel(y_predict)


if __name__ == '__main__':
    from split_data import create_dataset

    X_train, X_test, Y_train, Y_test = create_dataset('../dataset/dataset.csv')

    train(X_train, Y_train, '../result/reading_regression.pkl')

    test('../result/reading_regression.pkl', X_test.ix[:, 2:], Y_test)
