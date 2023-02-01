from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

#  set categories equal to the list ['rec.sport.baseball', 'rec.sport.hockey']
emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'])

print(emails.target_names)
print(emails.data[5])
print(emails.target[5])

train_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'],subset='train',shuffle = True,random_state = 108)

test_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'],subset='test',shuffle = True,random_state = 108)

# Create a CountVectorizer object
counter = CountVectorizer()
# Include all possible words can exist in our emails
counter.fit(test_emails.data + train_emails.data)
train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)

# Make a Naive Bayes classifier
classifier = MultinomialNB()
# Fit training set
classifier.fit(train_counts,train_emails.target)
accuracy = classifier.score(test_counts,test_emails.target)

# The accuracy of model
print(f'The accuraacy of model is {round(accuracy*100,2)} %')




