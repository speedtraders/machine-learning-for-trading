import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data\\csvs\\AACG.csv", delimiter=",", index_col=False)
print(df.head)
df = df['Open']
# df.drop(columns=['Ticker'], inplace=True)
df = df.tail(365)

preds = []
y = []
for i in range(333):

    df_test = df.iloc[i+30]
    df_train = df.iloc[i:i+30]

    y_train = df_train.to_numpy()
    X_train = np.array(range(i, i+30)).reshape(-1, 1)

    y_test = df_test.reshape(-1, 1)
    X_test = np.array(i+30).reshape(-1, 1)

    print(f'Len of train: {len(X_train)} \n len of test: {len(X_test)}')

    reg = LinearRegression()

    reg.fit(X_train, y_train)

    # prediction
    preds.append(reg.predict(X_test)[0])
    y.append(y_test[0][0])

df_result = pd.DataFrame()
# df_result['Days'] = pd.DataFrame(X_test)
df_result['preds'] = preds
df_result['real'] = y

sns.lineplot(data=df_result)
plt.show()
