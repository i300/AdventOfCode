PRE_LENGTH = 25

def add_number(value, arr):
    new_arr = arr[1:]
    new_arr.append(value)
    return new_arr

def is_valid(value, numbers):
    for a in numbers:
        for b in numbers:
            if a == b:
                continue
            elif a+b == value:
                return True
    return False

def find_weakness(value, numbers, length=2):
    while length < len(numbers):
        for index, _ in enumerate(numbers[PRE_LENGTH:]):
            values = numbers[index:index+length]
            if sum(values) == value:
                return min(values) + max(values)
        length += 1

def find_invalid(numbers):
    working_numbers = numbers[:PRE_LENGTH]
    for num in numbers[PRE_LENGTH:]:
        if is_valid(num, working_numbers):
            working_numbers = add_number(num, working_numbers)
        else:
            return num

with open('input.txt', 'r') as input_file:
    numbers = [int(num.strip()) for num in input_file.readlines()]
    invalid_num = find_invalid(numbers)
    pair = find_weakness(invalid_num, numbers)
    print('Part 1: {}'.format(invalid_num))
    print('Part 2: {}'.format(pair))
