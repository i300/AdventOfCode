def checkPhrases(file):
	infile = open(file, 'r')

	validPhrases = 0
	for line in infile:
		# Remove newlines from string and split into phrase array
		line = line.replace("\n", "")
		phrases = line.split(" ")
		
		# Check if phrase is valid
		valid = True
		for phrase in phrases:
			if (phrases.count(phrase) > 1):
				valid = False

		if (valid):
			validPhrases += 1

	return validPhrases

if __name__ == "__main__":
	print checkPhrases("input.txt")