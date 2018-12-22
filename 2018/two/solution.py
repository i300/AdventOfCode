def common_letters(a, b):
    list_result = []

    for i in range(len(a)):
        if (a[i] == b[i]):
            list_result.append(a[i])
    
    return list_result

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
    print("Checksum: {}".format(checksum))

    found_common = False
    for i, box_id_1 in enumerate(box_ids):
        for box_id_2 in box_ids[i:]:
            common = common_letters(box_id_1, box_id_2)
            if (len(common) == len(box_id_1) - 1):
                print("Common letters: {}".format(''.join(common)))
                found_common = True
                break
        if (found_common):
            break