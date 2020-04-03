import numpy as np

def sigmoid(x):
	return (1/(1 + np.exp(-x)))

def derivative_sigmoid(x):
	return sigmoid(x) * (1 - sigmoid(x))

def relu(x):
	return np.maximum(0,x)

def derivative_relu(x):
	return np.array([1]) if  np.array_equal(x,np.maximum(0,x)) else np.array([0])

def leaky_relu(x):
	return x if np.array_equal(x,np.maximum(0,x)) else 0.01 * x

def derivative_leaky_relu(x):
	return np.array([1]) if  np.array_equal(x,np.maximum(0,x)) else np.array([0.01])	

def unit_step(x):
	return np.array([1]) if x > 0 else np.array([0])

def tanh(x):
	return (1 - np.exp(-2*x))/(1 + np.exp(-2*x))

def derivative_tanh(x):
	return 1 - tanh(x)**2