"""
Raw Python Code of Artificial Neuron.
This is the very basic code of artificial neuron.
Components of the basic Artificial Neuron : Inputs, Weights, Bias, Summation Function, Activation Function**
Reference : https://towardsdatascience.com/whats-the-role-of-weights-and-bias-in-a-neural-network-4cf7e9888a0f
Note : as for now ignore Activation Function.

< Other Codes >
Dynamic code : "basics1_artificial_neuron.py"
Using numpy  : "basics5_artificial_neuron(numpy).py"
"""

inputs = [1.3, 5.5, 3.1]
weights = [3.1, 2.1, 8.7]
bias = 3

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias

print(output)