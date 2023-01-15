# Supervised Learning Algorithms

### Linear Regression / Multiple Linear Regression
Linear regression analysis is used to predict the value of a dependent variable based on the value of another independent variable. This form of analysis estimates the coefficients of the linear equation, involving one `linear regression` or more independent variables `multiple linear regression` that best predict the value of the dependent variable.

### Examples of linear regression:

* The market price of a house vs. the square footage of a house. Can we predict how much a house will sell for, given its size?
* The tax rate of a country vs. its GDP. Can we predict taxation based on a country’s GDP?
* The amount of chips left in the bag vs. number of chips taken. Can we predict how much longer this bag of chips will last, given how much people at this party have been eating?

Example of linear regression:

````
from sklearn.linear_model import LinearRegression                                          # Import linear regression function from scikit-learn linear_model module
import matplotlib.pyplot as plt
import numpy as np

line_fitter = LinearRegression()                                                           # Create linear regression model

temperature = np.array(range(60, 100, 2))
print(temperature)
temperature = temperature.reshape(-1, 1)                                                  # Reshape to 2D array
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

line_fitter.fit(temperature,sales)                                                         # Fit the model with label 
sales_predict = line_fitter.predict(temperature) 
plt.plot(temperature, sales, 'o')
plt.plot(temperature, sales_predict, 'x')
plt.show()
````





### Logisitic Regression

### K-Neighbor-Nearest (KNN)

### Decision Tree



