import pickle as cPickle
import os
import pandas as pd


def save_spreadsheet(fpath, fname, l):
    rmse = pd.Series(l[0])
    training = pd.Series(l[1])
    test = pd.Series(l[2])

    df = pd.DataFrame({'RMSE': rmse.values, 'predicted': training.values, 'real': test.values})
    df.to_csv(os.path.join(fpath, fname + '.csv'), sep=";",  index=False)


def save_best(fpath, fname, l):
    cPickle.dump(l, open(os.path.join(fpath, fname + '.p'), "wb"))
