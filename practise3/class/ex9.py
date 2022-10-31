import numpy as np
from datapreprocess import DataPreprocessing
from regression import  PolynomialRegressionAnalysis

dp = DataPreprocessing()
dp.read_from_csv()
dp.set_attributes_and_output()
# YOUR CODE FOR CREATING (X_train, X_test, y_train, y_test)
X_train, X_test, y_train, y_test=dp.final_train_test_data( attributes_list=[2,4,5], test_size=0.2)
# Step 1: Initialize a polynomial regressor with degree 2 (a model) to learn from data
pr=PolynomialRegressionAnalysis(2)

# Step 2: The regressor will learn from the input and output of training data
pr.fit(X_train, y_train)

# Step 3: After learning from training data, the model will make a prediction based on input testing data
y_pred=pr.predict(X_test)

# Step 4: Comparision and visualization
# class pr:
#     def mean_square_error(y_test,y_pred):
#         return sum([(x-y)**2 for x,y in zip(y_test,y_pred)])/len(y_test)
print('First 10 instances prediction (rounded to 1 decimal place):', np.array([round(i, 1) for i in y_pred[:10]]))
print('Real output of first 10 instances (rounded to 1 decimal place):', y_test[:10])
print('Mean square error (rounded to 1 decimal place):', round(pr.mean_square_error(y_test, y_pred),1))
