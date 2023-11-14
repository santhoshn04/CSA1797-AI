import random
def sigmoid(x):
    return 1 / (1 + pow(2.71828, -x))
def sigmoid_derivative(x):
    return x * (1 - x)
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.weights_input_hidden = [[random.uniform(-1, 1) for _ in range(self.hidden_size)] for _ in range(self.input_size)]
        self.bias_hidden = [random.uniform(-1, 1) for _ in range(self.hidden_size)]
        self.weights_hidden_output = [[random.uniform(-1, 1) for _ in range(self.output_size)] for _ in range(self.hidden_size)]
        self.bias_output = [random.uniform(-1, 1) for _ in range(self.output_size)]
    def forward(self, input_data):
        hidden_input = [0] * self.hidden_size
        for i in range(self.hidden_size):
            for j in range(self.input_size):
                hidden_input[i] += input_data[j] * self.weights_input_hidden[j][i]
            hidden_input[i] += self.bias_hidden[i]
        hidden_output = [sigmoid(x) for x in hidden_input]
        output_input = [0] * self.output_size
        for i in range(self.output_size):
            for j in range(self.hidden_size):
                output_input[i] += hidden_output[j] * self.weights_hidden_output[j][i]
            output_input[i] += self.bias_output[i]
        predicted_output = [sigmoid(x) for x in output_input]
        return predicted_output
input_size = 2
hidden_size = 4
output_size = 1
nn = NeuralNetwork(input_size, hidden_size, output_size)
input_data = [0.1, 0.9]
predicted_output = nn.forward(input_data)
print("Predicted Output:", predicted_output)
