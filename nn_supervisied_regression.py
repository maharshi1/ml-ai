# Supervisied Regression
# Prediciting the ratio of no. of hrs from sleep to study will result \
# into highest score.

import numpy as np
import matplotlib.pyplot as plt

# Sample data
# x = [no. hrs of sleep, no. hrs of study]
x = np.array(([3,5], [5,1], [10,2]), dtype=float)

# y = [test score]
y = np.array(([75], [82], [93]), dtype=float)

# Scaling the inputs
x = x / np.amax(x, axis=0)
y = y / 100 # Max test score

# 2 input layers(x) and a output layer(y) in this particular case.
# Whatever comes between these layers are called as hidden layers, \
# these are the deep belifs networks giving rise to deep learning.

# To solve this problem 1 hidden layer with 3 hidden units will do.
# Note: Circles represent neurons and lines represent synapses.
#       Synapses take a value from their input and multiply it by a \
#       specific weight and output the result.
#       Neurons on the other hand add all the output form their \
#       synapses and apply an activation function.
#            z = x1 + x2 + x3 = sum(xi)
#            a = 1 / 1 + e^-z 

class NeuralNetwork(object):

    # z2 = xW1 -- (1) 
    # a2 = f(z2) -- (2) 
    # z3 = a2.W2 -- (3)
    # yHat = f(z3) -- (4)

    def __init__(self):
        # Define HyperParameters : Are constans that establish the \
        # structure and behaviour of the network but are not updated \
        # as we train the network. 
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3

        # Weights (Parameters)
        self.W1 = np.random.rand(self.inputLayerSize, \
                                self.hiddenLayerSize)
        self.W2 = np.random.rand(self.hiddenLayerSize, \
                                self.outputLayerSize)

    def forward(self, x):
        # Propogate inputs through network
        self.z2 = np.dot(x, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat

    # Activation function
    def sigmoid(self, z):
        # Apply sigmoid activation function to scalar, vertor, or
        return 1 / (1 + np.exp(-z))

# At this point estimates are terrible as we have not trained the network.
NN = NeuralNetwork()
yHat = NN.forward(x)
# import pdb;pdb.set_trace()
ind = np.arange(len(y))
actualsocre = np.hstack(y)
estimatedscore = np.hstack(yHat)
ax = plt.subplot(111)
estimatedscore_bar = ax.bar(ind, estimatedscore, width=0.09, color='r')
actualsocre_bar = ax.bar(ind + 0.09, actualsocre, width=0.09, color='g')
plt.title('Cost of Error')
plt.ylabel('Scores')
plt.xlabel('[hrs of sleep, hrs of study]')
plt.xticks(ind + 0.09 / 2, x * np.amax(x, axis=0))
plt.legend((estimatedscore_bar[0], actualsocre_bar[0]), \
            ('Estimated', 'Actual'))
plt.show()

# To impove the model we first need to quantify excatly how wrong are \
# predictions are. Can be done by the cost function
#    J = cost = sum(1/2*(y-yHat)^2) -- (5)
# As the above equation is derived from 1,2,3, and 4, thus
#    J = sum(1/2*(y - f(f(xW1)W2))^2)
# What is the rate of change of J with respect to W, also kown as the \
# deretive(dJ/dW) since we are considering one weight at a time this \
# is partial derevative. 
# If dJ/dW is positive then the cost function is going up.
# If dJ/dW is negative then the cost function is going down.
# When going down, stopping at lowest min. is called  Gradient Descent.

class NeuralNetworkOptimized(NeuralNetwork):
    def costFunction(self, x, y):
        #Compute cost for given x,y, use weights already stored in class.
        self.yHat = self.forward(x)
        J = 0.5*sum((y-self.yHat)**2)
        return J

    def sigmoidPrime(self, z):
        # Derivative of Sigmoid Function
        return np.exp(-z) / ((1+np.exp(-z))**2)

    def costFunctionPrime(self, x, y):
        # Compute derivative with respect to W1 and W2
        self.yHat = self.forward(x)

        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)

        delta2 = np.dot(delta3, self.W2.T) * self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(x.T, delta2)

        return dJdW1, dJdW2

NN = NeuralNetworkOptimized()
import pdb;pdb.set_trace()
cost1 = NN.costFunction(x,y)
dJdW1, dJdW2 = NN.costFunctionPrime(x,y)
print dJdW1 
print dJdW2