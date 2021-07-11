import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import tensorflow
from true import *
from false import *

data = pd.read_csv("data.csv", sep=",")
data = data[["polarization", "truth", "sub_obj"]]

predict = "truth"

X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])

X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, test_size = 0.1)

linear = linear_model.LinearRegression()

linear.fit(X_train, Y_train)



predictions = linear.predict(X_test)

for X in range(len(predictions)):
    print(round(predictions[X]), ",", Y_test[X])


