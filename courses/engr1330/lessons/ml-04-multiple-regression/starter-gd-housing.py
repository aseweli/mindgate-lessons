import numpy as np
import pandas as pd

data = pd.read_csv("housing.csv")
features = ["Income", "HouseAge", "Population"]
su = []
for f in features:
    data[f + "_su"] = (data[f] - np.mean(data[f])) / np.std(data[f])
    su.append(f + "_su")

np.random.seed(1330)
shuffled = data.sample(len(data), replace=False)
train, test = shuffled.iloc[0:400], shuffled.iloc[400:]
X_train = np.vstack((np.ones((1, len(train))), train[su].values.T))
y_train = train["Price"].values.reshape(-1, 1)
X_test = np.vstack((np.ones((1, len(test))), test[su].values.T))
y_test = test["Price"].values.reshape(-1, 1)

theta = np.zeros((4, 1))
alpha, m = 0.05, len(train)
for i in range(2000):
    h = (theta.T @ X_train).T
    # TODO: update theta with the gradient-descent rule  theta - alpha * X_train @ (h - y_train) / m

def rmse(X, y):
    return np.sqrt(np.mean(((theta.T @ X).T - y) ** 2))

print("theta:", np.round(theta.ravel()))
print("train RMSE:", round(rmse(X_train, y_train)))
print("test RMSE:", round(rmse(X_test, y_test)))
