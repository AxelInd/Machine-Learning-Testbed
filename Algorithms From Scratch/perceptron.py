# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:44:16 2021

@author: axelt
"""
import numpy as np


def activationFunction_sigmoid (value):
    return 1.0/(1+np.e**(-1*value))
class perceptron (object):
    ACTIVATIONFUNCTIONS = {"sigmoid":activationFunction_sigmoid}
    def __init__(self,weights,_activationFunction="sigmoid"):
        self.activationFunction = perceptron.ACTIVATIONFUNCTIONS[_activationFunction]
        self.weights=weights
        
    def process(self,_input):
        #h = x_1 * w_1 + ... + x_n * w_n
        total = sum(_input*self.weights)
        return self.activationFunction(total)
    def update (self, _input, target, learningRate=0.4):
        #update rule: w_i = w_i + learning rate * (target-output)*x_i
        for i in range (0, len(self.weights)):
            self.weights[i]=self.weights[i]+learningRate*(target-self.process(_input))*_input[i]

if __name__ == "__main__":
    _input = np.array([5,6,7,8,9], dtype="float")
    target = 1
    _input = _input/sum(_input)
    weights = np.random.rand(len(_input))
    print (weights)
    print (_input)
    p = perceptron(weights)
    
    output = p.process(_input)
    print ("Initital Output is ", output)
    
    GENERATIONS = 1000
    LEARNINGRATE = 0.3
    
    for i in range (0, GENERATIONS):
        p.update(_input,target,LEARNINGRATE)
    output = p.process(_input)
    print ("Trained Output is ", output)