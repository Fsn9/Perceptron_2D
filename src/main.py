import numpy as np
import Perceptron as p
import matplotlib.pyplot as plt
import utilities as ut

# IMPLEMENTATION OF A 2D PERCEPTRON
epochs = 50000
train_set = [np.array([[0],[0]]),np.array([[0],[1]]),np.array([[1],[0]]),np.array([[1],[1]])]
learning_rate = 0.1

perceptron = p.Perceptron('leaky_relu','AND',learning_rate,epochs,train_set)

cost_history = perceptron.train()

perceptron.test()

ut.plot([x for x in range(len(cost_history))],'epochs',cost_history,'cost')


