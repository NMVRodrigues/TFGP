
import os
import pandas as pd
import numpy as np

path = '.' + os.sep + 'sheets'+ os.sep

files = []
extend = files.extend
for (dirpath, dirnames, filenames) in os.walk(path):
    extend(filenames)
    break

df_arr = []
appendDF = df_arr.append
for f in files:
    df = pd.read_csv(os.path.join(path + f), sep=';', engine='python')
    appendDF(df)


rmse = []
predicted = []
real = []


for dtf in df_arr:
    rmse.append(dtf['MAE'])
    predicted.append(dtf['predicted'])
    real.append(dtf['real'])


rmse = pd.concat(rmse, axis=1)
predicted = pd.concat(predicted, axis=1)
real = pd.concat(real, axis=1)

rmse = rmse.T
real = real.T
predicted = predicted.T
line_saparator = pd.Series([np.nan])

pd.concat([line_saparator, rmse, line_saparator, predicted, line_saparator, real]).to_csv(os.path.join(path, "10fold_dt_synNon0_500g" + '.csv'), sep=";",  index=True)
