import numpy as np
import activation_functions as af
import utilities as ut
from random import choice

MAXIMUM_TESTS = 15
PLOT_SAMPLING = 1
LEARNED_ENOUGH = 5

class Perceptron():
	def __init__(self, activation_function, model, learning_rate, epochs, train_set):
		self.weights = np.random.rand(1,2) * 2 - 1 # mean 0, between -1 and 1
		self.activation_function = activation_function
		self.model = model
		self.learning_rate = learning_rate
		self.bias = 0
		self.epochs = epochs
		self.train_set = train_set
		self.cost_history = []

	def __str__(self):
		return(
		str('my weights: ')+
		str(self.weights)+'\n'+
		str('my bias:')+
		str(self.bias)+'\n'+
		str('model to learn: ')+
		str(self.model)+'\n'+
		str('activation_function: ')+
		str(self.activation_function)+'\n'
		)

	def train(self):
		for epoch in range(self.epochs):
			x = choice(self.train_set)		
			predicted_output,z = self.feed_forward(x)
			cost = self.back_propagate(x,predicted_output,z)

			if epoch % PLOT_SAMPLING == 0:
				self.cost_history.append(sum(cost[0].tolist()))

			# check if already learned
			learned_enough,accuracy = self.learned_enough()
			if learned_enough:
				print('it needed',epoch,'epochs to learn out of',self.epochs,'\naccuracy: ',accuracy,'%\n')
				break

		return self.cost_history

	def learned_enough(self):
		accuracy = self.test_check()
		if accuracy < LEARNED_ENOUGH:
			return True, accuracy
		else:
			return False, accuracy

	def test_check(self):
		overall_cost = 0
		for each in self.train_set:
			_,_,cost = self.predict(each)
			overall_cost += cost
		return 100 * abs(overall_cost[0][0]) / len(self.train_set)

	def test(self):
		print('TEST:\n')
		for _ in range(MAXIMUM_TESTS):
			x = choice(self.train_set)
			prediction,expected,cost = self.predict(x)
			print('input:',x)
			print('output:',prediction)
			print('expected:',expected)
			print('cost:',cost,'\n')

	def predict(self,x):
		predicted,z = self.feed_forward(x)
		expected = ut.ground_truth(x,self.model)
		return predicted,expected,abs((predicted - expected))

	def feed_forward(self,x):
		if self.activation_function == 'sigmoid':
			# z = weighted sum
			z = np.dot(self.weights,x) + self.bias
			# a = activation function
			a = af.sigmoid(z)
			# y = output
			y = a
		elif self.activation_function == 'heavyside':
			# z = weighted sum
			z = np.dot(self.weights,x) + self.bias
			# a = activation function
			a = af.heavyside(z)
			# y = output 
			y = a
		elif self.activation_function == 'relu':
			# z = weighted sum
			z = np.dot(self.weights,x) + self.bias
			# a = activation function
			a = af.relu(z)
			# y = output 
			y = a
		elif self.activation_function == 'leaky_relu':
			# z = weighted sum
			z = np.dot(self.weights,x) + self.bias
			# a = activation function
			a = af.leaky_relu(z)
			# y = output 
			y = a
		elif self.activation_function == 'tanh':
			# z = weighted sum
			z = np.dot(self.weights,x) + self.bias
			# a = activation function
			a = af.tanh(z)
			# y = output 
			y = a
		return y,z

	def back_propagate(self,x,predicted,z):
		expected = ut.ground_truth(x,self.model)
		cost = 0.5 * (predicted - expected)**2

		if self.activation_function == 'sigmoid':
			dCost_da = predicted - expected
			da_dz = af.derivative_sigmoid(z)
			dz_dw = x
			dz_db = 1

			self.weights -= self.learning_rate * np.dot(np.multiply(dCost_da,da_dz),dz_dw.T)
			self.bias -= self.learning_rate * np.multiply(dCost_da,da_dz) * dz_db

		elif self.activation_function == 'heavyside':	
			error = predicted - expected

			self.weights -= self.learning_rate * error * x.T
			self.bias -= self.learning_rate * error

		elif self.activation_function == 'relu':	
			dCost_da = predicted - expected
			da_dz = af.derivative_relu(z)
			dz_dw = x
			dz_db = 1

			self.weights -= self.learning_rate * np.dot(np.multiply(dCost_da,da_dz),dz_dw.T)
			self.bias -= self.learning_rate * np.multiply(dCost_da,da_dz) * dz_db

		elif self.activation_function == 'leaky_relu':	
			dCost_da = predicted - expected
			da_dz = af.derivative_leaky_relu(z)
			dz_dw = x
			dz_db = 1

			self.weights -= self.learning_rate * np.dot(np.multiply(dCost_da,da_dz),dz_dw.T)
			self.bias -= self.learning_rate * np.multiply(dCost_da,da_dz) * dz_db

		elif self.activation_function == 'tanh':	
			dCost_da = predicted - expected
			da_dz = af.derivative_tanh(z)
			dz_dw = x
			dz_db = 1

			self.weights -= self.learning_rate * np.dot(np.multiply(dCost_da,da_dz),dz_dw.T)
			self.bias -= self.learning_rate * np.multiply(dCost_da,da_dz) * dz_db
	
		return cost

	def print_results(self):
		print('equation model learned:\n',self.weights[0][0],'x1 + ',self.weights[0][1],'x2',' +',self.bias[0][0])
