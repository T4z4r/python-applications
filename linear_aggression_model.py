from sklearn.linear_model import LinearRegression
import numpy as np

X=np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y=np.dot(X, np.array([1, 2])) + 3
reg=LinearRegression().fit(X, y)
print(f"Coefficients: {reg.coef_}")
print(f"Intercept: {reg.intercept_}")