import numpy as np # linear algebra
import matplotlib.pyplot as plt
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
train_data = pd.read_csv("/kaggle/input/titanic/train.csv")
#test_data = pd.read_csv("/kaggle/input/titanic/test.csv")

mytrain_data = train_data.copy()
# siblings_cnt = []
# survive_group = []
chardata = []
for i in range(max(mytrain_data['SibSp'])+1):
    tmp1 = sum(mytrain_data.loc[mytrain_data.SibSp == i]["Survived"])
    tmp2 = len(mytrain_data.loc[mytrain_data.SibSp == i])
    if(tmp2 == 0):
        continue
    else: 
        chardata.append(tmp1/tmp2)


plt.plot(chardata)
plt.xlabel('Siblings #')
plt.ylabel('Survived %')
plt.show()
