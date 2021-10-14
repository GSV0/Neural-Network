"""
Simple Python Code for Neuron Network Layer
Here We defining layer of 3 Neuron (having a 4 input and 3 output)
--------------------------------------------
 (input) >---
                }-- (Neuron) --> (output)
 (input) >---
                }-- (Neuron) --> (output)
 (input) >---
                }-- (Neuron) --> (output)
 (input) >---
--------------------------------------------

< Other Codes >
Using numpy : basics6_neuron_layer(numpy).py
"""


def neuron_layer(inputs, weights, biases):
    output_layer = list()
    for weight, bias in zip(weights, biases):
        output_layer.append(sum([i * w for i, w in zip(inputs, weight)]) + bias)
    return output_layer


if __name__ == '__main__':

    output = neuron_layer(

        # Inputs
        [1, 2, 3, 2.5],

        # Weights
        [[0.2, 0.8, -0.5, 1.0],
         [0.5, -0.91, 0.26, -0.5],
         [-0.26, -0.27, 0.17, 0.87]],

        # Biases
        [2, 3, 0.5]
    )
    print(output)