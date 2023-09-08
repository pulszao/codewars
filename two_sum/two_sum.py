def two_sum(numbers, target):
    i = -1

    for number in numbers:
        j = 0
        i += 1
        for aux_number in numbers[1:]:
            j += 1
            if (number + aux_number) == target:
                return [i, j]
