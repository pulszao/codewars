def unique_in_order(sequence):
    seq = []

    if len(sequence) > 1:
        seq = [sequence[0]]

    if len(sequence) == 1:
        return list(sequence)

    for i in range(0, len(sequence)):
        if seq[-1] != sequence[i]:
            seq.append(sequence[i])

    return seq