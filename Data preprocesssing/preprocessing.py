import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1    importing data set
df=pd.read_csv(r"E:\ML\Unihance\Data preprocesssing\Data.csv")
x=df.iloc[:, :-1].values
y=df.iloc[: , -1].values

df.hist(bins=20, figsize=(15,15))
plt.show

# 2    taking care of missing data
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan, strategy='mean')
x[:,1:3]=imputer.fit_transform(x[:,1:3])
# imputer.fit(x[:, 1:3])
# x[:, 1:3]=imputer.transform(x[:, 1:3])
print(x)

# 3  encoding indpendant variable

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])],remainder= 'passthrough')
x=np.array(ct.fit_transform(x))
print(x)

# 4 encoding dependant variable           (categorical data)  # labelencoder
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(y)
print(y)

# 5 spliting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test=train_test_split(x,y, test_size=0.2, random_state=1)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

# 6 Feature Scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train[:, 3:]=sc.fit_transform(x_train[:,3:])
x_test[:, 3:]=sc.transform(x_test[:,3:])                   #   m3mlt4 fit l test set 3l4an my7sl4 overfitting