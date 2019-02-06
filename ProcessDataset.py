import numpy as np
import pandas as pd
import sys


def load_data(fname):
    # reads into dataframe
    df = pd.read_csv(fname, dtype=np.float64, engine='python', header=None)
    y = df.iloc[:,-1].values
    X = df.values[:, list(range(0,len(df.columns)-1))]
    y = binarize_labels(y)
    X = normalize_features(standardize_features(X))
    new_df = np.column_stack((X,y))
    pd.DataFrame(new_df).to_csv(fname[:-4] + '_processed.csv', header=None, index=None)
       

def binarize_labels(Y):
    c = Y[0]
    norm = []
    for y in Y:
        if y == c:
            norm.append(0)
        else:
            norm.append(1)
    return norm


# converts scientific notation to float
def standardize_features(X):
    column_average = X.mean(0)
    std_deviation = X.std(0)
    for i in range(len(X)):
        X[i] = np.true_divide(np.subtract(X[i], column_average), std_deviation)
    return X


def normalize_features(X):
    maxV = X.max()
    minV = X.min()
    for i in range(len(X)):
        X[i] = (X[i] - minV) / (maxV - minV)
    return X


def main():
    load_data(sys.argv[1])


if __name__ == "__main__":
    main()
