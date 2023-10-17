import numpy as np
from sklearn.preprocessing import add_dummy_feature


theta_best = np.array([[4.21509616],
       [2.77011339]])
X_new_b = np.array([[1, 0], [1, 2]])

y_predict = X_new_b @ theta_best
print(y_predict)
