with open("two/input.txt", "r") as box_ids_file:
    box_ids = [box_id.strip() for box_id in box_ids_file.readlines()]

    num_two_repeating = 0
    num_three_repeating = 0
    for box_id in box_ids:
        letters = {}
        for char in box_id:
            if (char in letters):
                letters[char] = letters[char] + 1
            else:
                letters[char] = 1

        found_two_repeating = False
        found_three_repeating = False
        for v in letters.values():
            if (v == 2):
                found_two_repeating = True
            elif (v == 3):
                found_three_repeating = True

        if (found_two_repeating):
            num_two_repeating += 1
        if (found_three_repeating):
            num_three_repeating += 1
    
    checksum = num_two_repeating * num_three_repeating
    print(checksum)