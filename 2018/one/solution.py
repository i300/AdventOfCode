with open("one/input.txt", "r") as freqs_file:
    freqs = [freq.strip() for freq in freqs_file.readlines()]

    totalFreq = 0
    for freq in freqs:
        if (freq != ''):
            totalFreq += int(freq.strip())

    print(totalFreq)