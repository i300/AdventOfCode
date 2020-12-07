import re

parseMainRule = r'(\w+ \w+) bags contain (.*)'
parseSubrule = r'(\d) (\w+ \w+)'
def parseRule(rule):
    mainRuleResults = re.search(parseMainRule, rule)
    mainRuleKey = mainRuleResults.group(1)
    subrules = mainRuleResults.group(2).split(', ')
    
    mainRuleValue = {}
    for subrule in subrules:
        if subrule == 'no other bags.':
            break
        subruleResults = re.search(parseSubrule, subrule)
        subruleKey = subruleResults.group(2)
        subruleValue = subruleResults.group(1)
        mainRuleValue[subruleKey] = int(subruleValue)
    
    return mainRuleKey, mainRuleValue

def findRulesWithTarget(rulesDict, target):
    def doSearch(rulesDict, target, startingKey):
        targetCount = 0
        for otherKey, otherValue in rulesDict[startingKey].items():
            if otherKey == target or doSearch(rulesDict, target, otherKey):
                return 1
        
        return 0
    
    targetCount = 0
    for key in rulesDict.keys():
        targetCount += doSearch(rulesDict, target, key)

    return targetCount

def findTargetSize(rulesDict, target, startingSize=0):
    size = startingSize
    for key, value in rulesDict[target].items():
        size += findTargetSize(rulesDict, key, 1) * value

    return size

with open('input.txt', 'r') as input_file:
    rules = [rule.strip() for rule in input_file.readlines()]

    # Create rules object
    rulesDictionary = {}
    for rule in rules:
        key, value = parseRule(rule)
        rulesDictionary[key] = value
    
    print('Part 1: {}'.format(findRulesWithTarget(rulesDictionary, 'shiny gold')))
    print('Part 2: {}'.format(findTargetSize(rulesDictionary, 'shiny gold')))
