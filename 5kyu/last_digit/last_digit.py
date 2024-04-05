def last_digit(base, exponent):
    # Repetition standards
    # [0, 1, [4, 8, 6, 2], [9, 7, 1, 3], [6, 4, 6, 4], 5, 6, [9, 3, 1, 7], [4, 2, 6, 8], [1, 9, 1, 9]]
    if exponent == 0:
        return 1

    last_base_digit = base % 10
    if last_base_digit in (0, 1, 5, 6):
        return last_base_digit

    last_exp_digit = exponent % 4 + 4  # Add 4 because of the 4 repetitions of the standard and to avoid the power of 0

    return (last_base_digit ** last_exp_digit) % 10
