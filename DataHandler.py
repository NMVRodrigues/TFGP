import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import gc
'''
    File that manages the data inputs
'''


def load_data(fname):
    print("Parsing Data...")
    # reads into dataframe
    df = pd.read_csv(fname, dtype=np.float64, engine='python', header=None)
    # shuffles da dataset
    df = shuffle(df, random_state=None)
    # splits into labels and features
    X = df.values[:, list(range(0, len(df.columns)))]
    # splits into training and test
    train_set, test_set = train_test_split(X, test_size=0.3, shuffle=False)
    # splits test_set into features and labels
    test_y = tf.convert_to_tensor(test_set[:, -1])
    test_x = list(map(tf.convert_to_tensor, np.delete(test_set, -1, axis=1).T))
    # splits train_set into features and labels
    train_y = tf.convert_to_tensor(train_set[:, -1])
    train_x = list(map(tf.convert_to_tensor, np.delete(train_set, -1, axis=1).T))
    gc.collect()

    return train_x, train_y, test_x, test_y



