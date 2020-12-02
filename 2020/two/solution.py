import re

policyRegex = r'(?P<min>\d+)-(?P<max>\d+) (?P<char>[a-z]): (?P<pass>[a-z]+)'
def parsePolicy(policy):
    result = re.search(policyRegex, policy)
    minx = int(result.group('min'))
    maxx = int(result.group('max'))
    char = result.group('char')
    pwrd = result.group('pass')
    return minx, maxx, char, pwrd

def validPolicyA(policy):
    minx, maxx, char, pwrd = parsePolicy(policy)
    numChars = len([c for c in pwrd if c == char])
    return numChars >= minx and numChars <= maxx

def validPolicyB(policy):
    minx, maxx, char, pwrd = parsePolicy(policy)
    if (pwrd[minx-1] is char and pwrd[maxx-1] is not char):
        return True
    elif (pwrd[minx-1] is not char and pwrd[maxx-1] is char):
        return True
    else:
        print(policy)
        return False

with open("input.txt", "r") as policy_file:
    policies = [policy.strip() for policy in policy_file.readlines()]

    numValidPoliciesA = len([x for x in [validPolicyA(policy) for policy in policies] if x])
    numValidPoliciesB = len([x for x in [validPolicyB(policy) for policy in policies] if x])
    print("Part 1: {}".format(numValidPoliciesA))
    print("Part 2: {}".format(numValidPoliciesB))