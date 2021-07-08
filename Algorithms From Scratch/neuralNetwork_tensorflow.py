# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 12:21:22 2021

@author: axelt
Based on: https://www.youtube.com/watch?v=JdXxaZcQer8&list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf&index=10
Neural network to add numbers together
"""

# get data
# process data
# split data
# create network (ann + layers)
# select optimizer and loss function
# model.fit(x.train,y.train)
# model.evaluate(x.test,y.test)


import numpy as np
from sklearn.model_selection import train_test_split

#generate a dataset of numbers to be added together (x) and their sums per sample (y)
def generateDataset (numInputs, numSamples):
    x = np.array([[np.random.rand()/numInputs for i in range (0,numInputs)] for j in range (0, numSamples)])
    y = np.array([np.sum(i) for i in x])
    return x,y

x,y = generateDataset(2, 20000)

"""
print(x)
print (y)
"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

"""
print ("x_train", x_train)
print ("y_train", y_train)
print ("x_test",x_test)
print ("y_test",y_test)
"""

import tensorflow as tf

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(5, input_dim=2, activation="sigmoid"),
  tf.keras.layers.Dense(1, activation="sigmoid")
])

# choose optimiser (in this case, stochastic gradient descent)
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

# compile model (with mean squared error loss)
model.compile(optimizer=optimizer, loss='mse')

# train model
model.fit(x_train, y_train, epochs=100)

# evaluate model on test set
print("\nEvaluation on the test set:")
model.evaluate(x_test,  y_test, verbose=1)

# get predictions
data = np.array([[0.1, 0.2], [0.2, 0.2]])
predictions = model.predict(data)

# print predictions
print("\nPredictions:")
for d, p in zip(data, predictions):
    print("{} + {} = {}".format(d[0], d[1], p[0]))
