import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import datetime

style.use('ggplot')
arr = []
Open, High, Low, Close, Volume, MRC = [],[],[],[],[],[]

with open('d:/batData.txt') as fh:
    line = fh.readlines()
    for i in line:
        x = i.split('xx')
        Open.append(x[0])
        High.append(x[1])
        Low.append(x[2])
        Close.append(x[3])
        Volume.append(x[4])
        MRC.append(x[5].rstrip())

Open = Open[::-1]
High = High[::-1]
Low = Low[::-1]
Close = Close[::-1]

d = {'Open':Open,'High':High,'Low':Low,'Close':Close,'Volume':Volume,'MRC':MRC}
df = pd.DataFrame(data=d)
df = df[['Open','High','Low','Close','Volume','MRC']]

forecast_col = 'Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.04*len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

x = np.array(df.drop(['label'],1))
x = preprocessing.scale(x)
x_lately = x[-forecast_out:]
x = x[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])

x_train,x_test,y_train,y_test = cross_validation.train_test_split(x,y,test_size=0.2)
clf = LinearRegression(n_jobs=-1)
clf.fit(x_train,y_train)
accuracy = clf.score(x_test, y_test)

forecast_set = clf.predict(x_lately)
df['Forecast'] = np.nan

print(forecast_set,accuracy,forecast_out)

last_date = df.iloc[-1].name
last_unix = 1400630400
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df=df.astype(float)
print(df['Close'])
df['Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
