# Supervised Learning Algorithms

## Linear Regression 
Linear regression analysis is used to predict the value of a dependent variable based on the value of another independent variable. 

#### Examples of linear regression:

* The market price of a house vs. the square footage of a house. Can we predict how much a house will sell for, given its size?
* The tax rate of a country vs. its GDP. Can we predict taxation based on a country’s GDP?
* The amount of chips left in the bag vs. number of chips taken. Can we predict how much longer this bag of chips will last, given how much people at this party have been eating?

#### Points and Lines

![](https://lh3.googleusercontent.com/YPI2s5tug4qsSeQ0Q6CBD6Jj53wxmLo_2ECg-mUlzjxbysqs2YwTtN8NS5gFHBYK1mmL6NGCqdgDpsf_zUJo23gkB0smrIvR49ML-Hou) 

`m` is the slope<br/>
`b` is the intercept<br/>
`y` is a given point on the y-axis, and it corresponds to a given `x` on the x-axis<br/>

#### Gradient Descent for Intercept

![](https://lh3.googleusercontent.com/ViGB8iHBaTpd60abMmmJFboFJ_faTjMYWWlVlWrzypMcMA_RFMbV1fXrCd78NK7W7qb-ZTkVuurg6FT7FC1pdMP0LkanqLQlTrMjl1kKcQ)

`N` is the number of points we have in our dataset<br/>
`m` is the current gradient guess<br/>
`b` is the current intercept guess<br/>

#### Gradient Descent for Slope

![](https://lh3.googleusercontent.com/ZZ-UXSrWLE-ltMaeKbNP6Ysgx2mrZHUq6APTXxft8F7EqrgzcxRvj-14xrP2zami83apDojhw4riymIt6bj5RWWBfLaaZXqcBEyCs9de)

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

## Logisitic Regression
Logistic regression is a supervised machine learning algorithm that predicts the probability, ranging from 0 to 1, of a datapoint belonging to a specific category, or class.

#### Examples of logistic regression:
* Disease identification — Is a tumor malignant?
* Real or spam email?
* Customer conversion — Will a customer arriving on a sign-up page enroll in a service?

#### logit link function
![](https://lh3.googleusercontent.com/G4ABSO-DX-LZl1i6QOH7jS0lKRupH3cF-bMPLoZts9UK3Kvz32shLjVjlLD08S2dNqDZtb2B0HzGd305MOQ83B9Tpd1G5leQ42MprUgo)

#### Classification Threshold 
Once we have this probability, we need to make a decision about what class a datapoint belongs to. This is where the `classification threshold` comes in!
![](https://lh3.googleusercontent.com/JQEHIq4V8cDXHp4D7pMgWiHGCTAqULN6_Mxa6m9Zcv2GAKFT2xMrta5hqOleNZSYfvwAo8A7pT9Ax14l5LRWOES9FjaITgDr5mI09-g5)



### K-Neighbor-Nearest (KNN)

### Decision Tree



