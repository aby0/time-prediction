"""
This function creates test set, training set and saves them in a file and CV set out of the formed csv file
containing feature vectors.
"""

import pandas as pd
from sklearn.model_selection import train_test_split


"""
    INPUT : Single dataset
    OUTPUT : Training dataset, Testing dataset
"""


def create_dataset(filename):
    df = pd.read_csv(filename)
    df_x = df.ix[:, :-1]
    df_y = df.ix[:, -1:]
    x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)

    x_train_fin = x_train.ix[:, 2:]

    return x_train_fin, x_test, y_train, y_test


if __name__ == '__main__':
    create_dataset("../dataset/dataset.csv")
