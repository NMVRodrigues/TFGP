import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif
from sklearn.model_selection import train_test_split
import csv


def load_data(fname):
    # reads into dataframe
    df = pd.read_csv(fname, dtype=np.float64, engine='python', header=None)
    y = df.iloc[:,-1].values
    table_X = table_X[:, list(range(0,len(df.columns)-1))]
    #np.concatenate([a,b.reshape([len(b),1])],1)
    df = df.values
    ncols = len(df[0])
    new_df = 
    for col in range(ncols):
        pas
    

    
    




def BinarizeLabels(Y):
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
