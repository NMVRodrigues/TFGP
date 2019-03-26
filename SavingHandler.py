import pickle as cPickle
import os
import pandas as pd


def save_spreadsheet(fpath, fname, l):
    rmse = pd.Series(l[0])
    training = pd.Series(l[1])
    test = pd.Series(l[2])
    nodes = pd.Series(l[3])
    # mutP = tuple([x[0] for x in sublist[3]])
    # crossP = tuple([x[1] for x in sublist[3]])
    # mutP = pd.Series(mutP)
    # crossP = pd.Series(crossP)
    # df = pd.DataFrame({'training':training.values, 'test':test.values,'nodes':nodes.values,
    #                                   'crossoverP':crossP.values, 'MutationP':mutP.values})
    df = pd.DataFrame({'RMSE': rmse.values, 'training': training.values, 'test': test.values, 'nodes': nodes.values})
    df.to_csv(os.path.join(fpath, fname + '.csv'), sep=";",  index=False)


def save_best(fpath, fname, l):
    cPickle.dump(l, open(os.path.join(fpath, fname + '.p'), "wb"))
