import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle



def train_test_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[test_indices], data.iloc[train_indices]

if __name__ == '__main__':
	df = pd.read_csv('data.csv')
	test, train = train_test_split(df, 0.2)
	x_train =train[['fever','bodyPain', 'age', 'runnyNose', 'diffBreath']].to_numpy()
	x_test  =test[['fever','bodyPain', 'age', 'runnyNose', 'diffBreath']].to_numpy()

	y_train =train[['infectionProb']].to_numpy().reshape(2415 ,)
	y_test = test[['infectionProb']].to_numpy().reshape(603 ,)

	clf = LogisticRegression()
	clf.fit(x_train, y_train)

	file = open('model.pkl', 'wb')
	pickle.dump(clf, file) 
	file.close()
	



