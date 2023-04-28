# Supervised Learning Algorithms

## Linear Regression / Multiple Linear Regression
Linear regression analysis is used to predict the value of a dependent variable based on the value of another independent variable. This form of analysis estimates the coefficients of the linear equation, involving one `linear regression` or more independent variables `multiple linear regression` that best predict the value of the dependent variable.

### Examples of linear regression:

* The market price of a house vs. the square footage of a house. Can we predict how much a house will sell for, given its size?
* The tax rate of a country vs. its GDP. Can we predict taxation based on a country’s GDP?
* The amount of chips left in the bag vs. number of chips taken. Can we predict how much longer this bag of chips will last, given how much people at this party have been eating?

#### Points and Lines

y = m*x+c 

`m` is the slope<br/>
`b` is the intercept<br/>
`y` is a given point on the y-axis, and it corresponds to a given `x` on the x-axis<br/>

#### Gradient Descent for Intercept

![](images/gradient_descent.png)

`N` is the number of points we have in our dataset<br/>
`m` is the current gradient guess<br/>
`b` is the current intercept guess<br/>

#### Gradient Descent for Slope

![](images/gradient_descent_slope.png)

`N` is the number of points you have in your dataset.<br/>
`m` is the current gradient guess.<br/>
`b` is the current intercept guess.<br/>

#### Linear Regression in Scikit-learn

```
from sklearn.linear_model import LinearRegression

line_fitter = LinearRegression()
line_fitter.fit(X, y)

y_predicted = line_fitter.predict(X)
```

The .fit() method gives the model two variables that are useful to us:

`line_fitter.coef_`, which contains the slope<br/>

`line_fitter.intercept_`, which contains the intercept.<br/>







### Logisitic Regression

### K-Neighbor-Nearest (KNN)

### Decision Tree



