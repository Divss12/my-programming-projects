import numpy as np 
class NeuralNetwork():
    def __init__(self,layers):
        self.weights = [np.random.standard_normal(s)/(s[1]**0.5) for s in [(a,b) for a,b in zip(layers[1:],layers[:-1])] ]
        self.biases = [np.zeros((t,1)) for t in layers[1:]]
    def predict(self, a):
        for w,b in zip(self.weights,self.biases):
            a = self.activation(np.matmul(w,a) + b)
        return a 
    act = lambda x : 1/(1+np.exp(-x))
    @staticmethod
    def act(x):
        return 1/(1+np.exp(-x))