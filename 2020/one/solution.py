def findTwo2020(vals):
    for a in vals:
        for b in vals:
            if (int(a) + int(b) == 2020):
                return int(a)*int(b)

def findThree2020(vals):
    for a in vals:
        for b in vals:
            if (int(a) + int(b) < 2020):
                for c in vals:
                    if (int(a) + int(b) + int(c) == 2020):
                        return int(a)*int(b)*int(c)

with open("input.txt", "r") as freqs_file:
    vals = [val.strip() for val in freqs_file.readlines()]
    print("Result: {}".format(findTwo2020(vals)))
    print("Result: {}".format(findThree2020(vals)))