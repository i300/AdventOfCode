import re

polymer = ""
with open("five/input.txt", "r") as polymer_file:
    polymer = polymer_file.readline().strip()

def reduce_polymer(polymer):
    regex = r"((aA)|(Aa)|(bB)|(Bb)|(cC)|(Cc)|(dD)|(Dd)|(eE)|(Ee)|(fF)|(Ff)|(gG)|(Gg)|(hH)|(Hh)|(iI)|(Ii)|(jJ)|(Jj)|(kK)|(Kk)|(lL)|(Ll)|(mM)|(Mm)|(nN)|(Nn)|(oO)|(Oo)|(pP)|(Pp)|(qQ)|(Qq)|(rR)|(Rr)|(sS)|(Ss)|(tT)|(Tt)|(uU)|(Uu)|(vV)|(Vv)|(wW)|(Ww)|(xX)|(Xx)|(yY)|(Yy)|(zZ)|(Zz))"

    x = ["{0}{1}".format(c, c.upper()) for c in "abcdefghijklmnopqrstuvwxyz"]
    y = ["{1}{0}".format(c, c.upper()) for c in "abcdefghijklmnopqrstuvwxyz"]
    reductions = x + y

    while True:
        reduced_polymer = polymer

        # regex method
        # matches = re.findall(regex, reduced_polymer)
        # for reduction in matches:
        #     for match in reduction:
        #         if (match != ''):
        #             reduced_polymer = reduced_polymer.replace(match, "")

        # simple string replace method
        for reduction in reductions:
            reduced_polymer = reduced_polymer.replace(reduction, "")
        
        # check if we reduced. if we did, return reduction. if not, keep looping.
        if (reduced_polymer == polymer):
            return reduced_polymer
        else:
            polymer = reduced_polymer

# reduce original polymer
reduced_polymer = reduce_polymer(polymer)
print("Polymer Length: {}".format(len(reduced_polymer)))

# attempt to reduce polymer further by removing a unit type
smallest_polymer_len = len(polymer)
for unit in "abcdefghijklmnopqrstuvwxyz":
    trimmed_polymer = polymer.replace(unit, "")
    trimmed_polymer = trimmed_polymer.replace(unit.upper(), "")
    
    reduced_polymer = reduce_polymer(trimmed_polymer)
    if (len(reduced_polymer) < smallest_polymer_len):
        smallest_polymer_len = len(reduced_polymer)

print("Smallest Polymer Length: {}".format(smallest_polymer_len))
