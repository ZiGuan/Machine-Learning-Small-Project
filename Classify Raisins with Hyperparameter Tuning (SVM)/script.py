import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from skopt import BayesSearchCV
from skopt.space import Categorical, Real
from tpot import TPOTClassifier


# Load the data set
raisins = pd.read_csv('Classify Raisins with Hyperparameter Tuning (SVM)/Raisin_Dataset.csv')

X = raisins.drop('Class', axis=1)
y = raisins['Class']

# Split the data set into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Create an SVC model
svm = SVC()

# Dictionary of parameters for GridSearchCV
parameters = {'C':[1,10,100],'kernel':['linear','rbf','sigmoid']}
# Create a GridSearchCV model
grid = GridSearchCV(svm,parameters)
# Fit the GridSearchCV model to the training data
grid.fit(X_train,y_train)

#  the model and hyperparameters obtained by GridSearchCV
print(grid.best_estimator_)

#  a table summarizing the results of GridSearchCV
df = pd.concat([pd.DataFrame(grid.cv_results_['params']), pd.DataFrame(grid.cv_results_['mean_test_score'], columns=['Score'])], axis=1)
 
cv_table = df.pivot(index='kernel', columns='C')
print(cv_table)
#  the accuracy of the final model on the test data
print(grid.score(X_test,y_test))

# Dictionary of parameters for BayesSearchCV
search_spaces = {'kernel': Categorical(['linear', 'rbf', 'sigmoid']), 'C': Real(1, 100, prior='uniform')}
# Create a BayesSearchCV model
bayes = BayesSearchCV(svm, search_spaces, n_iter=10)

# Fit the BayesSearchCV model to the training data
bayes.fit(X_train, y_train)
# Print the model and hyperparameters obtained by BayesSearchCV
print(bayes.best_estimator_)
# Print the accuracy of the final model on the test data
print(bayes.score(X_test, y_test))

# Create a TPOTClassifier model
tpot = TPOTClassifier(generations=2, population_size=5, verbosity=2)
# Fit the TPOTClassifier model to the training data
tpot.fit(X_train, y_train)

# Print the accuracy of the final model on the test data
print(tpot.score(X_test, y_test))

# Export TPOTClassifier's final model to a separate file
tpot.export('tpot_pipeline.py')
