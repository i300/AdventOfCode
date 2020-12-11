import math

def find_diffs(adapters):
    diffs = {}
    for i, val in enumerate(adapters[:-1]):
        diff = adapters[i + 1] - adapters[i]
        diffs[diff] = diffs.setdefault(diff, 0) + 1

    return diffs[1], diffs[3]

# needed to google for this one :(
def find_num_possibilities(adapters):
    cache = { 0: 1 }

    for adapter in sorted(adapters):
        for diff in range(1, 4):
            next_adapter = adapter + diff
            if next_adapter in adapters:
                cache[next_adapter] = cache.setdefault(next_adapter, 0) + cache[adapter]
    
    return cache[max(adapters)]

with open('input.txt', 'r') as input_file:
    adapters = [int(num.strip()) for num in input_file.readlines()]
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()
    
    ones, threes = find_diffs(adapters)
    num_possibilities = find_num_possibilities(adapters)
    print('Part 1: {}'.format(ones * threes))
    print('Part 2: {}'.format(num_possibilities))
