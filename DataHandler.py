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


