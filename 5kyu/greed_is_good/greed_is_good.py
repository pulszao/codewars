def score(dice):
    occurrences = [0, 0, 0, 0, 0, 0]
    points = 0

    for num in dice:
        occurrences[num - 1] += 1

    index = 1
    for occurrence in occurrences:
        if index == 1:
            if occurrence >= 3:
                points += 1000
                occurrences[0] -= 3

        elif index == 2:
            if occurrence >= 3:
                points += 200

        elif index == 3:
            if occurrence >= 3:
                points += 300

        elif index == 4:
            if occurrence >= 3:
                points += 400

        elif index == 5:
            if occurrence >= 3:
                points += 500
                occurrences[4] -= 3

        elif index == 6:
            if occurrence >= 3:
                points += 600

        index += 1

    if occurrences[0] > 0:
        points += occurrences[0] * 100

    if occurrences[4] > 0:
        points += occurrences[4] * 50

    return points
