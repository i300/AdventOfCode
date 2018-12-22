import part1

memory = {0: {0: 1}}

def setValue(x, y, v):
	try:
		row = memory[x]
	except KeyError:
		memory[x] = {}

	memory[x][y] = v

def getValue(x, y):
	try:
		return memory[x][y]
	except KeyError:
		return 0

def getNeighborValues(x, y):
	return getValue(x - 1, y - 1) + getValue(x - 0, y - 1) + getValue(x + 1, y - 1) + getValue(x - 1, y - 0) + getValue(x + 1, y - 0) + getValue(x - 1, y + 1) + getValue(x - 0, y + 1) + getValue(x + 1, y + 1);

def getValueLargerThan(n):
	i = 2
	while True:
		position = part1.getPosition(i)
		thisValue = getNeighborValues(position[0], position[1])
		setValue(position[0], position[1], thisValue)
		if (thisValue > n):
			return thisValue
		
		i += 1

if __name__ == "__main__":
	print getValueLargerThan(277678)