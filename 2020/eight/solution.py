import copy

def parseInstruction(inst):
    return inst[0:3], int(inst[4:]), 0

def runComputer(instructions):
    acc = 0
    pc = 0
    while True:
        # check if we've gotten to the end of the program
        if (pc >= len(instructions)):
            return acc, 1
        
        # check if we've run an instruction twice (i.e. in an infinite loop)
        op, value, num_times = instructions[pc]
        if (num_times == 1):
            return acc, -1
        
        newpc = pc
        if op == 'nop':
            newpc += 1
        elif op == 'acc':
            acc += value
            newpc += 1
        if op == 'jmp':
            newpc += value

        instructions[pc] = (op, value, num_times + 1)          
        pc = newpc

def tryFixComputer(instructions):
    for i, inst in enumerate(instructions):
        new_instructions = copy.deepcopy(instructions)
        op, value, _ = inst
        if op == 'nop':
            new_instructions[i] = ('jmp', value, 0)
        elif op == 'jmp':
            new_instructions[i] = ('nop', value, 0)
        else:
            continue

        acc, result = runComputer(new_instructions)
        if result == 1:
            return acc, i
    
    return 0, 0

with open('input.txt', 'r') as input_file:
    raw_instructions = [instruction.strip() for instruction in input_file.readlines()]
    instructions = [parseInstruction(inst) for inst in raw_instructions]

    print('Part 1: {}'.format(runComputer(copy.deepcopy(instructions))))
    print('Part 2: {}'.format(tryFixComputer(copy.deepcopy(instructions))))
