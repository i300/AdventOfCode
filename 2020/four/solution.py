import re

def parsePassportEntries(passport):
    entries = [entry for entry in passport.replace('\n', ' ').strip().split(' ')]
    entries.sort()
    return entries

validPassports = [ ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'],  ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'] ]
def isValidPassportA(passport):
    entries = [entry[0:3] for entry in parsePassportEntries(passport)]
    return entries in validPassports

validHeight = r'^(\d)+(in|cm)$'
validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
validHairColor = r'^#(\d|[a-f]){6}$'
validPassportId = r'^\d{9}$'
def isValidPassportB(passport):
    if not isValidPassportA(passport):
        return False
    
    # build entries obj
    parsedEntries = parsePassportEntries(passport)
    entries = {}
    for entry in parsedEntries:
        key, value = entry.split(':')
        entries[key] = value
    
    # validate all
    if not (len(entries['byr']) == 4 and 1920 <= int(entries['byr']) <= 2002):
        print("Wrong byr: {}".format(entries['byr']))
        return False

    if not (len(entries['iyr']) == 4 and 2010 <= int(entries['iyr']) <= 2020):
        print("Wrong iyr: {}".format(entries['iyr']))
        return False

    if not (len(entries['eyr']) == 4 and 2020 <= int(entries['eyr']) <= 2030):
        print("Wrong eyr: {}".format(entries['eyr']))
        return False

    if not (re.search(validHeight, entries['hgt'])):
        print("Wrong HGT format: {}".format(entries['hgt']))
        return False

    if not ((entries['hgt'][-2:] == 'in' and 59 <= int(entries['hgt'][:-2]) <= 76)
            or (entries['hgt'][-2:] == 'cm' and 150 <= int(entries['hgt'][:-2]) <= 193)):
        print("Wrong HGT value: {}".format(entries['hgt']))
        return False

    if not (re.search(validHairColor, entries['hcl'])):
        print("Wrong HCL: {}".format(entries['hcl'] ))
        return False
    
    if not (entries['ecl'] in validEyeColors):
        print("Wrong ECL: {}".format(entries['ecl']))
        return False

    if not (re.search(validPassportId, entries['pid'])):
        print("Wrong PID: {}".format(entries['pid']))
        return False

    return True
        

with open("input.txt", "r") as passports_file:
    passports = "".join([passportLine for passportLine in passports_file.readlines()]).split("\n\n")

    print("Part 1: {}".format(len([x for x in [isValidPassportA(p) for p in passports] if x])))
    print("Part 2: {}".format(len([x for x in [isValidPassportB(p) for p in passports] if x])))
    