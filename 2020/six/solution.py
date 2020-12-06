def countAnswers(group):
    answers = set()
    for answer in group.replace(',', ''):
        answers.add(answer)
    return len(answers)

def countAllYesAnswers(groups):
    numGroups = len([group for group in groups.split(',') if group])
    answers = dict()
    for answer in groups.replace(',', ''):
        if answer in answers:
            answers[answer] += 1
        else:
            answers[answer] = 1

    return len([value for key,value in answers.items() if value == numGroups])
    
with open('input.txt', 'r') as input_file:
    groups = [group.replace('\n', ',').strip() for group in input_file.read().split('\n\n')]

    print("Part 1: {}".format(sum([countAnswers(group) for group in groups])))
    print("Part 2: {}".format(sum([countAllYesAnswers(group) for group in groups])))
