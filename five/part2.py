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
	# Calculate offset for jump
	delta = 0
	if (jumps[index] >= 3):
		delta = -1
	else:
		delta = 1

	# Store old index and jmp to next position
	oldIndex = index;
	index += jumps[index]

	# Increment old index by one and add 1 to counter
	jumps[oldIndex] += delta
	jmpCount += 1

print jmpCount