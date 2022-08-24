import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



df=pd.read_csv(r"E:\ML\Unihance\regression\simple linear_regression\Salary_Data.csv")
x=np.array(df.iloc[:,:-1].values).reshape(-1,1)
y=np.array(df.iloc[:,-1].values).reshape(-1,1)
print(x)
print(y)

#model spltting
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2 ,random_state=1 )


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
y_train=sc.fit_transform(y_train)
y_test=sc.transform(y_test)
# print(x_train)
# print(y_train)

#training model
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

#predict by test_set

y_predict=regressor.predict(x_test)

#visualization the training set
plt.figure()
plt.scatter(x_train, y_train, color='green')
plt.plot(x_train, regressor.predict(x_train), color='yellow' )
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()
# visualization the test dataset
plt.figure()
plt.scatter(x_test, y_test, color='red')
plt.plot(x_train, regressor.predict(x_train) ,color='black')
plt.xlabel('years of experience')
plt.ylabel('salary') 
plt.show()        