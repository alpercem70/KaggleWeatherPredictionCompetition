import pandas as p
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import linear_model

paths = ['train.csv', 'test.csv']
t = p.read_csv(paths[0])
t2 = p.read_csv(paths[1])

tfidf = TfidfVectorizer(max_features=10000, strip_accents='unicode', analyzer='word')
tfidf.fit(t['tweet'])
X = tfidf.transform(t['tweet'])
test = tfidf.transform(t2['tweet'])
y = np.array(t.ix[:,4:])

clf = linear_model.Ridge (alpha = .5)
clf.fit(X,y)
test_prediction = clf.predict(test)

print 'Train error: {0}'.format(np.sqrt(np.sum(np.array(np.array(clf.predict(X))-y)**2)/(X.shape[0]*24.0)))

prediction = np.array(np.hstack([np.matrix(t2['id']).T,test_prediction]))
col = '%i,' + '%f,'*23 + '%f'
np.savetxt('result.csv', prediction,col, delimiter=',')
