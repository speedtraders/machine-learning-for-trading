import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data\\csvs\\AACG.csv", delimiter=",", index_col=False)
print(df.head)
df = df['Open']
# df.drop(columns=['Ticker'], inplace=True)

df_test = df.tail(200)
df_train = df.drop(df.tail(200).index, inplace=False)

y_train = df_train.to_numpy()
X_train = np.array(range(len(y_train))).reshape(-1, 1)

y_test = df_test.to_numpy().reshape(-1, 1)
X_test = np.array(range(len(X_train), len(df))).reshape(-1, 1)

print(f'Len of train: {len(X_train)} \n len of test: {len(X_test)}')

reg = GradientBoostingRegressor(n_estimators=600,
                                max_depth=5,
                                learning_rate=0.01,
                                min_samples_split=3)

reg.fit(X_train, y_train)

# prediction
df_result = pd.DataFrame()
# df_result['Days'] = pd.DataFrame(X_test)
df_result['preds'] = reg.predict(X_test)
df_result['real'] = pd.DataFrame(y_test)

sns.lineplot(data=df_result)
plt.show()
