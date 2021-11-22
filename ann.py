import random
import string

NODE_COUNT_PER_LAYER = [3]

class Node:
    def __init__(self, children):
        self.children = children
        self.name = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        self.weights = []
        return

    def pretty_print(self, layer):
        indent = '  ' * layer
        if len(self.children) == 0:
            print(f"{indent}{self.name}")
            return
        print(f"{indent}{self.name} is connected to ")
        for i in range(len(self.children)):
                self.children[i].pretty_print(layer + 1)
                if i < len(self.weights):
                    print(f"{indent} with weight {self.weights[i]} ")
        return

class ANN:
    def __init__(self, node_count_per_layer):
        self.input_layer = []
        self.output_layer = []
        
        # make the different layers of nodes
        old_children = []
        new_children = []
        for i in range(len(node_count_per_layer) - 1, -1, -1):
            self.input_layer = []
            for j in range(0, node_count_per_layer[i]):
                newnode = Node(old_children)
                self.input_layer.append(newnode)
                if i == len(node_count_per_layer) - 1:
                    self.output_layer.append(newnode)
            old_children = self.input_layer
        return

    def pretty_print(self):
        for i in range(len(self.input_layer)):
            self.input_layer[i].pretty_print(0)
        return

    def set_random_weights(self):
        current_layer = self.input_layer
        while len(current_layer) > 0:
            for i in range(len(current_layer)):
                for j in range(len(current_layer[i].children)):
                    current_layer[i].weights.append(random.uniform(0, 1))
            current_layer = current_layer[0].children
        return
    
a = ANN([4, 3, 2])
a.pretty_print()
#print(a.input_layer)
#print(a.output_layer)
print("\nAdding random weights\n")
a.set_random_weights()
a.pretty_print()
