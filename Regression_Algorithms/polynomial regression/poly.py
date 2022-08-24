from typing import ClassVar
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


 #importing the data
df=pd.read_csv(r"E:\ML\Unihance\regression\polynomial regression\Position_Salaries.csv")
x=df.iloc[:,1:-1].values
y=df.iloc[:,-1].values


# plt.scatter(x ,y , color='red')
# plt.show()

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly=PolynomialFeatures(degree=4)
x_poly=poly.fit_transform(x)
lin_reg=LinearRegression()
lin_reg.fit(x_poly , y)


# x_grid=np.arange(min(x), max(y), 0.1)
# x_grid=x_grid.reshape(-1,1)
# plt.scatter(x , y , color='blue')
# plt.plot(x_grid, lin_reg.predict(poly.fit_transform(x_grid)), color='red')
# plt.show()

p1=lin_reg.predict(poly.fit_transform([[6.5]]))
print(p1)
