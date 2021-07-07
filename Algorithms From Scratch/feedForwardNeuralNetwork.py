# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 12:44:44 2021

@author: axelt
"""
import numpy as np

#the most common ANN activation function
def activationFunction_sigmoid (value):
    return 1.0/(1+np.e**(-1*value))

#inputs
x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#.reshape(-1,x) infers the size of the original 1d array for itself and makes it x dimensional instead
y = np.array([1,2]).reshape(-1,2)



#normalise
x = x/np.average(x)

#meta parameters
HIDDENLAYERSIZE = 4
OUTPUTSIZE = 1

#initialise random weights for each previous neuron to each subsequent one
hiddenLayer = np.random.rand(HIDDENLAYERSIZE,len(x[0]))
outputLayer = np.random.rand(HIDDENLAYERSIZE,OUTPUTSIZE)
hiddenLayer = np.array(hiddenLayer)
#print ("hidden layer\n",hiddenLayer)
#print ("output layer\n",outputLayer)

print ("hiddenLayer",hiddenLayer.shape)
print("outputLayer",outputLayer.shape)

# Dimensional process
# input -> hidden layer
# (2,5) -> (4,5) -- won't work so we need to transpose
# (2,5) * (5,4) -> (2,4)
# hidden layer -> output layer
# (2,4) * (4,1) -> (2,1) 

hiddenOutput = np.dot(x,hiddenLayer.T)

activatedHiddenOutput = activationFunction_sigmoid(hiddenOutput)
#print ("hiddenOutput\n",hiddenOutput)
#print ("activatedhiddenOutput\n",activatedHiddenOutput)

print ("activatedhiddenOutput shape", activatedHiddenOutput.shape)
print ("outputLayer shape", outputLayer.shape)
output = np.dot(activatedHiddenOutput,outputLayer)
finalOutput = activationFunction_sigmoid(output)

print ("Final output:\n",finalOutput)