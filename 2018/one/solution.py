with open("one/input.txt", "r") as freqs_file:
    freqs = [freq.strip() for freq in freqs_file.readlines()]
    foundFreqs = {}

    totalFreq = 0
    loopFreq = 0
    foundReapeatedFreq = False
    while not foundReapeatedFreq:
        loopFreq = 0
        for freq in freqs:
            if (freq != ''):
                totalFreq += int(freq)
                loopFreq += int(freq)
                if (totalFreq in foundFreqs and not foundReapeatedFreq):
                    print("Repeated Freq: {}".format(totalFreq))
                    foundReapeatedFreq = True
                foundFreqs[totalFreq] = "Y"
    
    print("Device Output: {}".format(loopFreq))