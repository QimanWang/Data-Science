import numpy as np
import pandas as pd
import math
import os
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pandas as pd
from ggplot import *

file = ""
files = [f for f in os.listdir('.') if os.path.isfile(f)]

for f in files:
    f = f.lower()
    if "bob" in f:
        file = f

msg = "found file: " + file
print(msg)


def create_ary(df, col_name, label):
    data_list = []
    label_list = []
    for index, row in df.iterrows():
        # print(str(row[col_name]))
        # print(str(row[col_name]) == 'empty')
        if str(row[col_name]) == 'empty':
            print('foundNAN')
            break
        else:
            data_list.append(row[col_name])
            label_list.append(label)
    return data_list, label_list


xl = pd.ExcelFile(file)
in_df = xl.parse()
in_df = in_df.fillna(value='empty')
col_names = list(in_df)

label = 0
big_dump = []
for col in col_names:
    # print(in_df[in_df.columns[0]])
    data_list, label_list = create_ary(in_df, col, label)
    label += 1
    big_dump.append(data_list)
    big_dump.append(label_list)

# make X0 before hand
precent_train = .7
print('before slicing', len(big_dump[0]))
X0_idx = len(big_dump[0]) * precent_train
X0_idx = math.ceil(X0_idx)
print('after', X0_idx)
X0train = big_dump[0][:X0_idx]
X0test = big_dump[0][X0_idx:]
y0train = big_dump[1][:X0_idx]
y0test = big_dump[1][X0_idx:]
print(X0train)
print(X0test)
print(y0train)
print(y0test)

# start loop to calculate roc
for i in range(1, (len(big_dump)) // 2):
    print('i', i)
    idx = 2 * i
    print('idx:', idx)
    print('length before spliting', len(big_dump[idx]))
    X_idx = math.ceil(len(big_dump[idx]) * precent_train)
    print('cut off idx', X_idx)
    Xtrain = big_dump[idx][:X_idx]
    Xtest = big_dump[idx][X_idx:]
    ytrain = big_dump[idx + 1][:X_idx]
    ytest = big_dump[idx + 1][X_idx:]
    # print('Xtrain', Xtrain)
    # print('Xtest', Xtest)
    # print('ytrain', ytrain)
    # print('ytest', ytest)
    Xtrain_total = X0train + Xtrain
    Xtest_total = X0test + Xtest
    ytrain_total = y0train + ytrain
    ytest_total = y0test + ytest

    Xtrain_total = np.asarray(Xtrain_total).reshape(-1, 1)
    Xtest_total = np.asarray(Xtest_total).reshape(-1, 1)
    ytrain_total = np.asarray(ytrain_total).reshape(-1, 1)
    ytest_total = np.asarray(ytest_total).reshape(-1, 1)
    # print('Xtrain', Xtrain_total)
    # print('Xtest', Xtest_total)
    # print('ytrain', ytrain_total)
    # print('ytest', ytest_total)

    # calculation time
    clf = LogisticRegression()
    clf.fit(Xtrain_total, ytrain_total)

    preds = clf.predict_proba(Xtest_total)[:, 1]
    fpr, tpr, _ = metrics.roc_curve(ytest_total, preds)

    df = pd.DataFrame(dict(fpr=fpr, tpr=tpr))
    ggplot(df, aes(x='fpr', y='tpr')) + \
    geom_line() + \
    geom_abline(linetype='dashed')