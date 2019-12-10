#Importing libraries
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Reading the data.csv using pandas
dataset = pd.read_csv('data.csv')

#Dividing the dependent and independent variables
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#Printing the new values
print(x)
print(y)

#Using Imputer/SimpleImputer for handle the missing data/values by mean strategy
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(x[:,1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

print(x)

#Using onehotencoding
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(), [0])],    # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
    remainder='passthrough'                         # Leave the rest of the columns untouched
)

x = np.array(ct.fit_transform(x), dtype=np.float)

print(x)

#Used Label Encoder
labelencoder_y = LabelEncoder()

y = labelencoder_y.fit_transform(y)
print(y)

#Model Test-Train Splitting

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#Feature Scaling Done Using Standard Scaler

sc_x = StandardScaler()


x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

print("\n")
print(x_train)
print(x_test)
