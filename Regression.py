import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn import neural_network
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


df = pd.read_csv('1.csv') 
#print(df.describe())
#print(df.head(5))
cols = list(df.columns.values)
X = df[cols[0:-2]]
Y = df[[cols[-1]]]
Y = Y.values.ravel()
#print(Y)
#print(X)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

model = linear_model.Ridge()
#model = SVR(C=10, epsilon=100)
#model = neural_network.MLPRegressor(random_state=10, max_iter=1000)
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
Y_test = np.array(Y_test)
fig, ax = plt.subplots()
#print(r2_score(Y_test,Y_pred))
print(Y_test[120],Y_pred[120])
ax.scatter(Y_pred, Y_test)
ax.set_title("Regression")
ax.set_xlabel("Y_pred")
ax.set_ylabel("Y_test")
lims = [
    np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
    np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
]
ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
ax.set_aspect('equal')
ax.set_xlim(lims)
ax.set_ylim(lims)
fig.savefig('1.png', dpi=300)

