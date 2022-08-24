import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.construct import rand


# importing data set
df= pd.read_csv(r"E:\ML\Unihance\Data preprocesssing\Data.csv")
x=df.iloc[:,:-1].values
y=df.iloc[:, -1].values
# df.hist(bins=20, figsize=(15,15))
# plt.show()

#missing data

from sklearn.impute import SimpleImputer
md=SimpleImputer(missing_values=np.nan, strategy='mean')
x[:,1:3]=md.fit_transform(x[:,1:3])
print(x)

# hot encoding 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
en=ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])],remainder='passthrough')
x=np.array(en.fit_transform(x))
print(x)

#label encoding
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=np.array(le.fit_transform(y))
print(y)

#spliting data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,train_size=0.2,random_state=1)

#data scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train[:,3:]=sc.fit_transform(x_train[:,3:])
x_test[:,3:]=sc.transform(x_test[:,3:])