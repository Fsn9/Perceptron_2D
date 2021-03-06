import numpy as np
import Perceptron as p
import matplotlib.pyplot as plt
import utilities as ut
# IMPLEMENTATION OF A 2D PERCEPTRON

# Parameters
epochs = 20000
train_set = [np.array([[0],[0]]),np.array([[0],[1]]),np.array([[1],[0]]),np.array([[1],[1]])]
learning_rate = 0.1
activation_function = 'leaky_relu'
model = 'NAND'

# Perceptron
perceptron = p.Perceptron(activation_function,model,learning_rate,epochs,train_set)

# train
cost_history = perceptron.train()

# test
perceptron.test()

# print results to the terminal
perceptron.print_results()

# plot the loss over epochs
ut.plot([x for x in range(len(cost_history))],'epochs',cost_history,'cost')

