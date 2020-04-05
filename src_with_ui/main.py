import numpy as np
import Perceptron as p
import matplotlib.pyplot as plt
import utilities as ut
import UserInterface as ui
import threading
import queue
# IMPLEMENTATION OF A 2D PERCEPTRON

# Parameters
epochs = 20000
train_set = [np.array([[0],[0]]),np.array([[0],[1]]),np.array([[1],[0]]),np.array([[1],[1]])]
learning_rate = 0.1
activation_function = 'leaky_relu'
model = 'NAND'

# Queue to be shared between perceptron and User Interface
q = queue.Queue()

# Perceptron
perceptron = p.Perceptron(activation_function,model,learning_rate,epochs,train_set)
perceptron_thread = threading.Thread(target = perceptron.run_perceptron)
perceptron_thread.start()

# User Interface
ui = ui.UserInterface(306,166,perceptron,perceptron_thread)
ui.mainloop()



