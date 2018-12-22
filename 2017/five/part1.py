# Setup data structures
jumps = []
index = 0

# Read input file and setup jump array
infile = open('input.txt', 'r')
for line in infile:
	jumps.append(int(line))

# Traverse maze
jmpCount = 0
while (index < len(jumps)):
	# Store old index and jmp to next position
	oldIndex = index;
	index += jumps[index]

	# Increment old index by one and add 1 to counter
	jumps[oldIndex] += 1
	jmpCount += 1

print jmpCount