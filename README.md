# Supervised Learning Algorithms

## Linear Regression 
`Linear regression` analysis is used to predict the value of a dependent variable based on the value of another independent variable. 

#### Examples of linear regression

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
`Multiple Linear Regression` uses two or more independent variables to predict the values of the dependent variable.

#### Examples of multiple linear regression
* Predicting the housing prices with many factors.
* Medical research to analyze the relationship between a dependent variable and various independent variables

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
`Logistic regression` is a supervised machine learning algorithm that predicts the probability, ranging from 0 to 1, of a datapoint belonging to a specific category, or class.

#### Examples of logistic regression
* Disease identification — Is a tumor malignant?
* Real or spam email?
* Customer conversion — Will a customer arriving on a sign-up page enroll in a service?

#### Logit Link Function
![](https://lh3.googleusercontent.com/G4ABSO-DX-LZl1i6QOH7jS0lKRupH3cF-bMPLoZts9UK3Kvz32shLjVjlLD08S2dNqDZtb2B0HzGd305MOQ83B9Tpd1G5leQ42MprUgo)

#### Classification Threshold 
Once we have this probability, we need to make a decision about what class a datapoint belongs to. This is where the `classification threshold` comes in!</br>

![](https://content.codecademy.com/programs/data-science-path/logistic-regression/Threshold-01.svg)

## K-Neighbor-Nearest (KNN)
`K-Nearest Neighbors (KNN)` is a classification algorithm. The central idea is that data points with similar attributes tend to fall into similar categories.

#### Examples of K-Neighbor-Nearest (KNN)
* Customer Segmentation: Group customers with similar characteristics together.
* Anomaly Detection: KNN can be used to detect anomalies or outliers in a dataset. 
* Breast Cancer Classifier

#### Distance Formula (Euclidean Distance)
`Euclidean Distance` was used to find the distance between each points and find the nearest point.
![](https://lh3.googleusercontent.com/JIV-_GU3ue1K99wvRLCrgC0zhpNpg3Zg9Fb-ZuFJ_EXVrwsQsQwlcJYqVJLTqH6MBrNvg21OZpt9bSHOqdZq1xlllglslt6N-ynOFEs0)

#### Three steps of the K-Nearest Neighbor Algorithm:
1. Normalize the data
2. Find the k nearest neighbors
3. Classify the new point based on those neighbors

## Decision Tree
`Decision trees` are machine learning models that try to find patterns in the features of data points. </br></br>
About the example below, the red points represent students that didn’t get an A on a test and the green points represent students that did get an A on a test.</br></br>
![](https://content.codecademy.com/programs/data-science-path/decision-trees/tree_gif.gif)

#### Examples of Decision Tree
* Credit Risk Assessment: Decision trees can be used to assess the credit risk of individuals or businesses.
* Disease Diagnosis: In the field of healthcare, decision trees can aid in diagnosing diseases. 
* Product Recommendation: Decision trees can be utilized in recommendation systems. 

#### Gini Impurity
`Gini impurity` is a measure of the impurity or disorder in a set of data used in the context of decision tree algorithms. It quantifies how well a randomly selected element from a set would be classified incorrectly if it were randomly labeled according to the distribution of labels in the set. </br>
![](https://lh3.googleusercontent.com/bLZGIDh9UHWnOAIPoZN3fqS9zJ5aWlhDTvDY3vfOaeQf04rFwn8tqppZ3-tFYODTzGdJoHVWjEfuQ7wQdenF1Jb8hfpT8ttcF-an4NVf) </br>
where `p(i)` represents the probability of an element.

## Naive Bayes Classifier

`Naive Bayes classifier` is a supervised machine learning algorithm that leverages Bayes’ Theorem to make predictions and classifications. </br></br>
Bayes’ Theorem: </br>
![](https://lh3.googleusercontent.com/TXhDQU3LU_CAUK4Vzy22PXSIGvIsLhq94ySIewTjbuBhvHzyX9HVy3u5nGN33WjBs2M6ahZ4rsjAaHS3kiLaC9QWK6Ce3ns6_rYeh3hD) </br>
This equation is finding the probability of `A` given `B`

#### Examples of Naive Bayes Classifier
* Spam Detection: Naive Bayes can be used to classify emails as either spam or non-spam.
* Sentiment Analysis: Naive Bayes can be employed to determine the sentiment of a given text, such as a product review or a social media post.
* Document Categorization: Naive Bayes can be used to automatically categorize documents into predefined categories. 

## Support Vector Machine (SVM)

`Support Vector Machine` makes classifications by defining a decision boundary and then seeing what side of the boundary an unclassified point falls on. Decision boundaries are easiest to wrap your head around when the data has two features.</br></br> 
Binary Classification: </br>
![](https://lh3.googleusercontent.com/3mkALoswcsALZEFug5zHulNyowEjYAfLQzzjs6tD9a5UrY7v4t5nDpqnSrpzHUSdOnHtebAzDlMoCfEew9HyevJvqvzHbZWtI9doxxqkJQ)
Multi-Classification: </br>
![](https://lh3.googleusercontent.com/aLH1TihJeXd0xS6UKlS6uN-VERKwDE3s4f1keOj9ULwWUpjireaFW66odOwLAf-QttTGRV9G8llttWmOmLxjteSEg2RFoi46XngiRD8uTg)

#### Examples of Support Vector Machine
* Text Classification: SVMs are commonly used for text classification tasks, such as sentiment analysis, spam detection, or topic categorization.
* Image Classification: SVMs can be used for image classification tasks, such as recognizing objects or distinguishing between different types of images. 
* Handwritten Digit Recognition: SVMs have been successfully applied to recognize handwritten digits. 

#### Support Vectors and Margins
`Support vectors` are the points in the training set closest to the decision boundary. `Margin` is the distance between a support vector and the decision boundary.

## Random Forest
`Random forest` is an ensemble machine learning technique. A `random forest` contains many decision trees that all work together to classify new points.

#### Examples of Random Forest
* Feature Importance: Random Forest can provide insights into the importance of different features in a dataset. 
* Missing Value Imputation: Random Forest can be used for imputing missing values in a dataset. 
* Recommender Systems: Random Forest can be used in recommender systems to suggest items or content to users based on their preferences. 

#### Bagging
`Random forests` create different trees using a process known as `bagging`, which is short for `bootstrapped aggregating`. 

## Boosting
`Boosting` is a sequential learning technique where each of the base models builds off of the previous model. Each subsequent model aims to improve the performance of the final ensemble model by attempting to fix the errors in the previous stage. </br>

There are two important decisions that need to be made to perform boosted ensembling:</br>
* Sequential Fitting Method
* Aggregation Method

#### Adaptive Boosting Overview

`Adaptive Boosting` (or `AdaBoost`) is a sequential ensembling method that can be used for both classification and regression. It can use any base machine learning model, though it is most commonly used with decision trees. </br></br>
For `AdaBoost`, the `Sequential Fitting Method` is accomplished by updating the weight attached to each of the training dataset observations as we proceed from one base model to the next. The `Aggregation Method` is a weighted sum of those base models where the model weight is dependent on the error of that particular estimator.</br></br>

#### Gradient Boosting Overview

`Gradient Boosting` is a sequential ensembling method that can be used for both classification and regression. It can use any base machine learning model, though it is most commonly used with decision trees, known as Gradient Boosted Trees.</br></br>
For `Gradient Boost`, the `Sequential Fitting Method` is accomplished by fitting a base model to the negative gradient of the error in the previous stage. The `Aggregation Method` is a weighted sum of those base models where the model weight is constant.</br></br>








