import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif
import csv
'''
    File that manages the data inputs
'''


# jms
def load_data(fname):
    df = pd.read_csv(fname, engine='python')
    table_X = df.as_matrix().astype(float)
    #
    table_y = table_X[:, len(df.columns)-1].astype(int)
    table_y = table_y.tolist()
    #table_y = [str(val) for val in table_y]
    #
    # assumindo que toas as colunas sao uteis e que a ultima sao as labels
    table_X = table_X[:, list(range(0,len(df.columns)-1))]
    print(table_X.shape)
    #table_X = SelectKBest(f_classif, k=72).fit_transform(table_X, table_y)
    #print(table_X.shape)
    #table_X = table_X.tolist()
    #table_X = [[str(val) for val in row] for row in table_X]
    #

    # encoder = LabelEncoder()
    # encoder.fit(table_y)
    # y = encoder.transform(table_y)
    # Y = one_hot_encode(y)
    #print(table_X.shape)


    features = df.columns.values
    features = np.delete(features,0)
    features = features.tolist()
    features.pop()
    #
    return table_X, table_y, features


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


def sci2floatFeatures(X):
    for row in X:
        for x in row:
            x = format(x, 'f')
    return X

def sci2floatLabels(X):
    for v in X:
        v = format(v, 'f')
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