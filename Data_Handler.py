import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif
from sklearn.model_selection import train_test_split
import csv
'''
    File that manages the data inputs
'''


def load_data(fname):
    # reads into dataframe
    df = pd.read_csv(fname, dtype=np.float64, engine='python', header=None)
    # shuffles da dataset
    df = shuffle(df,random_state=1)
    # split into training and test
    train, test = train_test_split(df, test_size=0.3, shuffle=False)
    # save tensors
    train_cols = []
    test_cols = []
    to_tensor = tf.convert_to_tensor
    appendTrn = train_cols.append
    appendTst = test_cols.append
    for i in range(len(train.columns)):
        appendTrn(to_tensor(train[i]))
    train_labels = train_cols.pop(-1)
    for i in range(len(test.columns)):
        appendTst(to_tensor(test[i]))
    test_labels = test_cols.pop(-1)

    return train_cols, train_labels, test_cols, test_labels


# makes labels 0 and 1
def normalizelabels(Y):
    c = Y[0]
    norm = []
    for y in Y:
        if y == c:
            norm.append(0)
        else:
            norm.append(1)
    return norm


# converts scientific notation to float
def standardizeFeatures(X):
    column_average = X.mean(0)
    std_deviation = X.std(0)
    for i in range(len(X)):
        X[i] = np.true_divide(np.subtract(X[i], column_average), std_deviation)
    return X

def normalizeFeatures(X):
    maxV = X.max()
    minV = X.min()
    for i in range(len(X)):
        X[i] = (X[i] - minV) / (maxV - minV)
    return X

# Reading the dataset
def read_dataset(fname):
    df = pd.read_csv(fname, engine='python')
    #print(len(df.columns))
    X = df[df.columns[0:60]].values
    y = df[df.columns[60]]

    # Encode the dependent variable
    encoder = LabelEncoder()
    encoder.fit(y)
    y = encoder.transform(y)
    Y = one_hot_encode(y)
    print(X.shape)
    return (X, Y)


# Define the encoder function.
def one_hot_encode(labels):
    n_labels = len(labels)
    n_unique_labels = len(np.unique(labels))
    one_hot_encode = np.zeros((n_labels, n_unique_labels))
    one_hot_encode[np.arange(n_labels), labels] = 1
    return one_hot_encode