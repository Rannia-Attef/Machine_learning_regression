import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the data
df=pd.read_csv(r"E:\ML\Unihance\regression\SVR\Position_Salaries.csv")
# df_1=df.info()
# print(df_1)
# df_2=df.head()
# print(df_2)
x=df.iloc[:, 1:-1].values
y=df.iloc[: , -1].values
y=y.reshape(-1 ,1 )


#preprocessing  1.. standar
from sklearn.preprocessing import StandardScaler
st_x=StandardScaler()
st_y=StandardScaler()
x=st_x.fit_transform(x)
y=st_y.fit_transform(y)
# print(x)
# print(Y)

from sklearn.svm import SVR
regressor= SVR(kernel='rbf',degree=6)
regressor.fit(x,y)


#to predict we can't use the same scalar
u=st_y.inverse_transform(regressor.predict(st_x.transform([[6.5]])))
print(u)

plt.scatter(st_x.inverse_transform(x)  , st_y.inverse_transform(y))
plt.plot(st_x.inverse_transform(x), st_y.inverse_transform(regressor.predict(x)))
plt.title('in reg by svr')
plt.xlabel('level')
plt.ylabel('salary')
plt.show()


