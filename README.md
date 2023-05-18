# Supervised Learning Algorithms

## Linear Regression 
Linear regression analysis is used to predict the value of a dependent variable based on the value of another independent variable. 

#### Examples of linear regression:

* The market price of a house vs. the square footage of a house. Can we predict how much a house will sell for, given its size?
* The tax rate of a country vs. its GDP. Can we predict taxation based on a country’s GDP?
* The amount of chips left in the bag vs. number of chips taken. Can we predict how much longer this bag of chips will last, given how much people at this party have been eating?

#### Points and Lines

y = mx+c 

`m` is the slope<br/>
`b` is the intercept<br/>
`y` is a given point on the y-axis, and it corresponds to a given `x` on the x-axis<br/>

#### Gradient Descent for Intercept

![](https://lh3.googleusercontent.com/prK671o6wzUPzCPCJEYfGgCXE27FcXP4D6xcx7zptaxJ88OyNvS7l33rC17Dl2J1dfV1IwyusXdO1qMil2oLbOr9RRP8YauxbMFaRnU)

`N` is the number of points we have in our dataset<br/>
`m` is the current gradient guess<br/>
`b` is the current intercept guess<br/>

#### Gradient Descent for Slope

![](images/gradient_descent_slope.png)

`N` is the number of points you have in your dataset.<br/>
`m` is the current gradient guess.<br/>
`b` is the current intercept guess.<br/>


## Multiple Linear Regression

Multiple Linear Regression uses two or more independent variables to predict the values of the dependent variable.

#### Multiple Linear Regression Equation
![](https://lh3.googleusercontent.com/xqfSqu2qKzaWXsVpjajlhETrxWl3Pmyn5f1oON1nm7IOv2JMSIz2NTRd8IfSb2I8nB5A6IYr-qEKV4Gu44qutvyctsSa77m6aJTNpKY)</br>

Here, `m1`, `m2`, `m3`, … mn refer to the coefficients, and `b` refers to the intercept that you want to find.

#### Training Set vs. Test Set

* `Training set`: the data used to fit the model
* `Test set`: the data partitioned away at the very start of the experiment (to provide an unbiased evaluation of the model)

![](images/set.png)

#### Residual Analysis

One of the technique can evaluate the accuracy of our multiple linear regression model.The difference between the actual value y, and the predicted value ŷ is the `residual e`. The equation is:

` e = y - ŷ `

### Logisitic Regression

### K-Neighbor-Nearest (KNN)

### Decision Tree



