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

def parse_node(data):
    num_subnodes = data.get_next_data()
    num_metadata = data.get_next_data()

    metadata_sum = 0
    for _ in range(num_subnodes):
        metadata_sum += parse_node(data)

    for _ in range(num_metadata):
        metadata_sum += data.get_next_data()

    return metadata_sum

if __name__ == "__main__":
    data = []
    with open("eight/input.txt", "r") as input_file:
        data = [int(x) for x in input_file.readline().strip().split(" ")]

    data_class = Data(data)
    sum_metadata = parse_node(data_class)
    print("Metadata Sum: {}".format(sum_metadata))
    