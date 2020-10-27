import NeuralNetwork as nn
import numpy as np 

layers = (3,5,10)

x = np.ones((layers[0],1))

net = nn.NeuralNetwork(layers)
pred = net.predict(x)

print(pred)