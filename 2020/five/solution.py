def parsePass(bp):
    row = int(bp[0:7].replace('F','0').replace('B','1'), 2)
    col = int(bp[7:].replace('L','0').replace('R','1'),2)
    return (row * 8) + col

def findSeat(seats):
    for seat in seats:
        if (seat + 1 not in seats and seat + 2 in seats):
            return seat + 1
    return 0

with open('input.txt', 'r') as passes_file:
    boardingPasses = [boardingPass.strip() for boardingPass in passes_file.readlines()]
    seatIds = [parsePass(bp) for bp in boardingPasses]
    print("Part 1: {}".format(max(seatIds)))
    print("Part 2: {}".format(findSeat(seatIds)))