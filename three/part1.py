import math

# Get the position of number n on a number spiral
# where (0, 0) = 1
def getPosition(n):
	# Current vector
	dx = 1
	dy = 0

	# Current position
	x = 0
	y = 0

	# Segment info
	segment_length = 1
	segment_step = 0

	# Transform to 0 index
	n = n - 1

	for k in range(n):
		x += dx
		y += dy

		segment_step += 1
		if (segment_step == segment_length):
			segment_step = 0

			# Rotate counter clockwise
			dx_old = dx;
			dx = -dy;
			dy = dx_old;

			if (dy == 0):
				segment_length += 1

	return (x, y)

posInput = getPosition(277678)

print abs(posInput[0]) + abs(posInput[1])