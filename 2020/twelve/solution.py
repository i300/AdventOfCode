import re
import numpy as np

def get_rotation_matrix(degrees):
    rad = degrees / 180 * np.pi
    return np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])

def parse_instruction(instr, current_pos, current_dir):
    command, value = instr[0], int(instr[1:])
    
    if command == 'N':
        return current_pos + (value * np.array([0, 1])), current_dir
    elif command == 'S':
        return current_pos + (value * np.array([0, -1])), current_dir
    elif command == 'E':
        return current_pos + (value * np.array([1, 0])), current_dir
    elif command == 'W':
        return current_pos + (value * np.array([-1, 0])), current_dir
    elif command == 'L':
        return current_pos, get_rotation_matrix(value).dot(current_dir)
    elif command == 'R':
        return current_pos, get_rotation_matrix(-value).dot(current_dir)
    elif command == 'F':
        return current_pos + (value * current_dir), current_dir

def parse_waypoint_instructions(instr, current_pos, current_waypoint):
    command, value = instr[0], int(instr[1:])
    
    if command == 'N':
        return current_pos, current_waypoint + (value * np.array([0, 1]))
    elif command == 'S':
        return current_pos, current_waypoint + (value * np.array([0, -1]))
    elif command == 'E':
        return current_pos, current_waypoint + (value * np.array([1, 0]))
    elif command == 'W':
        return current_pos, current_waypoint + (value * np.array([-1, 0]))
    elif command == 'L':
        return current_pos, get_rotation_matrix(value).dot(current_waypoint)
    elif command == 'R':
        return current_pos, get_rotation_matrix(-value).dot(current_waypoint)
    elif command == 'F':
        return current_pos + (value * current_waypoint), current_waypoint

def part1(instructions):
    current_pos = np.array([0, 0])
    current_dir = np.array([1, 0])
    for instr in instructions:
        current_pos, current_dir = parse_instruction(instr, current_pos, current_dir)
        current_dir = np.around(current_dir, 10)

    return np.sum(np.abs(current_pos))

def part2(instructions):
    current_pos = np.array([0, 0])
    current_wyp = np.array([10, 1])
    for instr in instructions:
        current_pos, current_wyp = parse_waypoint_instructions(instr, current_pos, current_wyp)
        current_wyp = np.around(current_wyp, 10)

    return np.sum(np.abs(current_pos))

with open('input.txt', 'r') as input_file:
    instructions = [line.strip() for line in input_file.readlines()]

    print('Part 1: {}'.format(part1(instructions)))
    print('Part 2: {}'.format(part2(instructions)))
