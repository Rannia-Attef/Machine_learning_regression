from numpy.core.fromnumeric import reshape
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv(r"E:\ML\Unihance\regression\multiple_linear regression\50_Startups.csv")
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
# print(x)
# print(y)
colum=df.columns
print(colum)
# df.info()
# df.hist(bins=10, figsize=(10,10))
# plt.show()


#..............encoding the dummy variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
en=ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[3])], remainder='passthrough')
x=np.array(en.fit_transform(x))
#print(x)

#.......split the data into train and test datasets
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2 , random_state=1)

#......algorithm
           # 1 training the train set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train, y_train)

             # 2 predict 
y_pred=regressor.predict(x_test)  
#print(y_pred)
np.set_printoptions(precision=2)
comp=np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1)        

#print(comp)

plt.figure()
plt.scatter(x_train , y_train , color='blue')
#plt.plot(x_train, regressor.predict(x_train))
plt.show()
