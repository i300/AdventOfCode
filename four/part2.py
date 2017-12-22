def checkPhrases(file):
	infile = open(file, 'r')

	validPhrases = 0
	for line in infile:
		# Remove newlines from string and split into phrase array
		line = line.replace("\n", "")
		phrases = line.split(" ")

		anagramList = []
		
		# Check if phrase is valid
		valid = True
		for phrase in phrases:
			# Check if phrase is unique
			if (phrases.count(phrase) > 1):
				valid = False

			# Check if phrase is an anagram of another phrase
			phraseList = list(phrase)
			phraseList.sort()
			sortedPhrase = ''.join(phraseList)
			if (sortedPhrase not in anagramList):
				anagramList.append(sortedPhrase)
			else:
				valid = False

		if (valid):
			validPhrases += 1

	return validPhrases

if __name__ == "__main__":
	print checkPhrases("input.txt")