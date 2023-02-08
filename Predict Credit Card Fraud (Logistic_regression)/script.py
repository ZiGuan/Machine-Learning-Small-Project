import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

cwd = os.getcwd()
print(cwd)

# Load the data
transactions = pd.read_csv('Predict Credit Card Fraud (Logistic_regression)/transactions_modified.csv')

print(transactions.head())
print(transactions.info())

# How many fraudulent transactions?

print(transactions['isFraud'].sum())

# Summary statistics on amount column
print(transactions['amount'].describe())

# Create isPayment field
transactions['isPayment'] = 0
transactions['isPayment'][transactions['type'].isin(['PAYMENT','DEBIT'])] = 1

# Create isMovement field
transactions['isMovement'] = 0
transactions['isMovement'][transactions['type'].isin(['CASH_OUT','TRANSFER'])] = 1

# Create accountDiff field
accountDiff = abs(transactions['oldbalanceOrg']-transactions['oldbalanceDest'])

# Create features and label variables
features = transactions[['amount','isPayment','isMovement','accountDiff']]
label = transactions['isFraud']

# Split dataset
x_train,x_test,y_train,y_test = train_test_split(features, label, train_size = 0.7, random_state = 6)

# Normalize the features variables
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Fit the model to the training data
model = LogisticRegression()
model.fit(x_train,y_train)

# Score the model on the training data
score_train = model.score(x_train,y_train)
print(score_train)

# Score the model on the test data
score_test = model.score(x_test,y_test)
print(score_test)

# Print the model coefficients
print(model.coef_)

# New transaction data
transaction1 = np.array([123456.78, 0.0, 1.0, 54670.1])
transaction2 = np.array([98765.43, 1.0, 0.0, 8524.75])
transaction3 = np.array([543678.31, 1.0, 0.0, 510025.5])

# Create a new transaction
your_transaction = np.array([20000.0, 0.0, 1.0, 502.0])

# Combine new transactions into a single array
sample_transactions = np.stack((transaction1,transaction2,transaction3,your_transaction))

# Normalize the new transactions
sample_transactions = scaler.transform(sample_transactions)

# Predict fraud on the new transactions
fraudulent = model.predict(sample_transactions)
print(fraudulent)

# Show probabilities on the new transactions
fraudulent_prob = model.predict_proba(sample_transactions)
print(fraudulent_prob)
