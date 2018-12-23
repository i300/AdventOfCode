class Data():
    index = 0
    data = []

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data[self.index]

    def get_next_data(self):
        data = self.data[self.index]
        self.inc_index()
        return data

    def get_index(self):
        return self.index
    
    def inc_index(self):
        self.index += 1
        return self.index

def calc_metadata_sum(data):
    num_subnodes = data.get_next_data()
    num_metadata = data.get_next_data()

    metadata_sum = 0
    for _ in range(num_subnodes):
        metadata_sum += calc_metadata_sum(data)

    for _ in range(num_metadata):
        metadata_sum += data.get_next_data()

    return metadata_sum

def calc_node_value(data):
    num_subnodes = data.get_next_data()
    num_metadata = data.get_next_data()
    node_value = 0

    if (num_subnodes == 0):
        for _ in range(num_metadata):
            node_value += data.get_next_data()
    else:
        subnode_values = []
        for _ in range(num_subnodes):
            subnode_values.append(calc_node_value(data))

        for _ in range(num_metadata):
            metadata_value = data.get_next_data()
            try:
                node_value += subnode_values[metadata_value - 1]
            except IndexError:
                pass
    
    return node_value

if __name__ == "__main__":
    data = []
    with open("eight/input.txt", "r") as input_file:
        data = [int(x) for x in input_file.readline().strip().split(" ")]

    data_class = Data(data)
    sum_metadata = calc_metadata_sum(data_class)
    print("Metadata Sum: {}".format(sum_metadata))

    data_class = Data(data)
    root_value = calc_node_value(data_class)
    print("Root Node Value: {}".format(root_value))