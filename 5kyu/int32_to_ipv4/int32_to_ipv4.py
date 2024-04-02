def int32_to_ip(int32):
    bin_list = []
    quotient = int32

    while True:
        remainder = quotient % 2
        quotient = quotient // 2

        bin_list.insert(0, str(remainder))

        if quotient == 0:
            break

    bin_list.reverse()
    bin_num = ''.join(bin_list)
    bin_num = bin_num.ljust(32, '0')

    index = 0
    ipv4 = []
    ip = 0
    for num in bin_num:
        if index == 8:
            index = 0
            ipv4.insert(0, str(ip))
            ip = 0

        ip += int(num) * pow(2, index)

        index += 1

    ipv4.insert(0, str(ip))

    return '.'.join(ipv4)


print(int32_to_ip(2154959208))
