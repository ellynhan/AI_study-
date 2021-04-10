import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
from os import walk
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font',family='AppleGothic') #한글사용
from sklearn.linear_model import LogisticRegression
_, _, filenames = next(walk('./data/'))
print(filenames)

train_data_1 = pd.read_csv("./data/1.csv")
train_data_1.head()

train_data_1.columns = ['산업분류별','행정구역별','사업체수','종사자수','남','여','매출액','영업비용','영업이익']
train_data_1 = train_data_1.iloc[1:]
train_data_1.head()

a = train_data_1[train_data_1['산업분류별']=='전산업']
plt.bar(a['행정구역별'],a['사업체수'])
plt.show()

numberOfBusiness = [int(line) for line in a["사업체수"]]
x = a["행정구역별"][1:]
y = numberOfBusiness[1:]
plt.bar(x, y)
plt.xticks(rotation=75)
for i,j in zip(x,y):
    plt.text(i,j,str(j), rotation=75, fontsize=8)
plt.title('지역별 사업체 수', y=1.1)
plt.show()

