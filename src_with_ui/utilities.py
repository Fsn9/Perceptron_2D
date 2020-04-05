import numpy as np
import matplotlib.pyplot as plt

def ground_truth(x,type_):
	if type_ == 'AND':
		if np.array_equal(np.array([[0],[0]]),x):
			return np.array([[0]])
		elif np.array_equal(np.array([[0],[1]]),x):
			return np.array([[0]])
		elif np.array_equal(np.array([[1],[0]]),x):
			return np.array([[0]])
		elif np.array_equal(np.array([[1],[1]]),x):
			return np.array([[1]])

	elif type_ == 'OR':
		if np.array_equal(np.array([[0],[0]]),x):
			return np.array([[0]])
		elif np.array_equal(np.array([[0],[1]]),x):
			return np.array([[1]])
		elif np.array_equal(np.array([[1],[0]]),x):
			return np.array([[1]])
		elif np.array_equal(np.array([[1],[1]]),x):
			return np.array([[1]])

	elif type_ == 'NAND':
		if np.array_equal(np.array([[0],[0]]),x):
			return np.array([[1]])
		elif np.array_equal(np.array([[0],[1]]),x):
			return np.array([[0]])
		elif np.array_equal(np.array([[1],[0]]),x):
			return np.array([[0]])
		elif np.array_equal(np.array([[1],[1]]),x):
			return np.array([[0]])
			
	elif type_ == 'XOR':
		if np.array_equal(np.array([[0],[0]]),x):
			return np.array([[0]])
		elif np.array_equal(np.array([[0],[1]]),x):
			return np.array([[1]])
		elif np.array_equal(np.array([[1],[0]]),x):
			return np.array([[1]])
		elif np.array_equal(np.array([[1],[1]]),x):
			return np.array([[0]])

def plot(x,x_label,y,y_label):
	plt.plot(x,y)
	plt.ylabel(y_label)
	plt.xlabel(x_label)
	plt.show()