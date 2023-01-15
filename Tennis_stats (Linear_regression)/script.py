import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os
print(os.getcwd())


# Import Data
tennis = pd.read_csv('Tennis_stats (Linear_regression)/tennis_stats.csv')
print(tennis.head())

#Plotting Data without training model
plt.scatter(tennis[['BreakPointsOpportunities']],tennis[['Winnings']],alpha =0.4)
plt.show()

# Training Model with FirstServeReturnPointsWon feature
x = tennis[['FirstServeReturnPointsWon']]
y = tennis[['Winnings']]

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,random_state=6)
model = LinearRegression()
model.fit(x_train,y_train)
y_predict = model.predict(x_test)

print(model.score(x_test,y_test))

plt.scatter(y_test, y_predict, alpha=0.4, color='red')
plt.show()

# Training Model with BreakPointsOpportunities feature and realise the high accuracy
x = tennis[['BreakPointsOpportunities']]
y = tennis[['Winnings']]

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,random_state=6)
model = LinearRegression()
model.fit(x_train,y_train)
y_predict = model.predict(x_test)

print(model.score(x_test,y_test))

plt.scatter(y_test, y_predict, alpha=0.4, color='red')
plt.title('Tennis Ace')
plt.xlabel('Test Result')
plt.ylabel('Predict Result')
plt.show()

# Training Model with two feature 
x = tennis[['BreakPointsOpportunities','FirstServeReturnPointsWon']]
y = tennis[['Winnings']]

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,random_state=6)
model = LinearRegression()
model.fit(x_train,y_train)
y_predict = model.predict(x_test)

print(model.score(x_test,y_test))

plt.scatter(y_test, y_predict, alpha=0.4, color='red')
plt.title('Tennis Ace')
plt.xlabel('Test Result')
plt.ylabel('Predict Result')
plt.show()

# Training Model with multiple feature 
x = tennis[['BreakPointsOpportunities','FirstServeReturnPointsWon','FirstServePointsWon','SecondServePointsWon','BreakPointsConverted']]
y = tennis[['Winnings']]

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,random_state=6)
model = LinearRegression()
model.fit(x_train,y_train)
y_predict = model.predict(x_test)

print(model.score(x_test,y_test))

plt.scatter(y_test, y_predict, alpha=0.4, color='red')
plt.title('Tennis Ace')
plt.xlabel('Test Result')
plt.ylabel('Predict Result')
plt.show()
















# # perform exploratory analysis here:






















# ## perform single feature linear regressions here:






















# ## perform two feature linear regressions here:






















# ## perform multiple feature linear regressions here:
