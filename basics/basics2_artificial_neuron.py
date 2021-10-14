"""
Raw Python Code of Artificial Neuron
Components of the basic Artificial Neuron : Inputs, Weights, Bias, Summation Function, Activation Function
Reference : https://towardsdatascience.com/whats-the-role-of-weights-and-bias-in-a-neural-network-4cf7e9888a0f
Note : as for now ignore Activation Function.
"""


def summation(inputs, weights, bias):
    return sum([i*w for i, w in zip(inputs, weights)])+bias


if __name__ == '__main__':
    output = summation([1.3, 5.5, 3.1], [3.1, 2.1, 8.7], 3)
    print(output)