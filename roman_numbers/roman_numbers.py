def get_roman(list, number, type):
    # TYPE == 1 -> thousand; == 2 -> hundreds; == 3 -> decimal; == 4 units;
    if type == 1:
        for num in range(0, number):
            list.append('M')

    else:
        if number == 1:
            if type == 2:
                list.append('C')
            elif type == 3:
                list.append('X')
            elif type == 4:
                list.append('I')

        elif number == 2:
            if type == 2:
                list.append('CC')
            elif type == 3:
                list.append('XX')
            elif type == 4:
                list.append('II')

        elif number == 3:
            if type == 2:
                list.append('CCC')
            elif type == 3:
                list.append('XXX')
            elif type == 4:
                list.append('III')

        elif number == 4:
            if type == 2:
                list.append('CD')
            elif type == 3:
                list.append('XL')
            elif type == 4:
                list.append('IV')

        elif number == 5:
            if type == 2:
                list.append('D')
            elif type == 3:
                list.append('L')
            elif type == 4:
                list.append('V')

        elif number == 6:
            if type == 2:
                list.append('DC')
            elif type == 3:
                list.append('LX')
            elif type == 4:
                list.append('VI')

        elif number == 7:
            if type == 2:
                list.append('DCC')
            elif type == 3:
                list.append('LXX')
            elif type == 4:
                list.append('VII')

        elif number == 8:
            if type == 2:
                list.append('DCCC')
            elif type == 3:
                list.append('LXXX')
            elif type == 4:
                list.append('VIII')

        elif number == 9:
            if type == 2:
                list.append('CM')
            elif type == 3:
                list.append('XC')
            elif type == 4:
                list.append('IX')


class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        thousand = int(val / 1000)
        hundreds = int((val / 100) % 10)
        decimal = int((val / 10) % 10)
        unity = int(val % 10)

        roman = []

        get_roman(roman, thousand, 1)
        get_roman(roman, hundreds, 2)
        get_roman(roman, decimal, 3)
        get_roman(roman, unity, 4)

        return ''.join(roman)

    @staticmethod
    def from_roman(roman_num: str) -> int:
        num = 0

        if 'IV' in roman_num:
            num += 4
            roman_num = roman_num.replace('IV', '', 1)
        if 'IX' in roman_num:
            num += 9
            roman_num = roman_num.replace('IX', '', 1)
        if 'XL' in roman_num:
            num += 40
            roman_num = roman_num.replace('XL', '', 1)
        if 'XC' in roman_num:
            num += 90
            roman_num = roman_num.replace('XC', '', 1)
        if 'CD' in roman_num:
            num += 400
            roman_num = roman_num.replace('CD', '', 1)
        if 'CM' in roman_num:
            num += 900
            roman_num = roman_num.replace('CM', '', 1)

        for char in roman_num:
            if char == 'M':
                num += 1000
                roman_num = roman_num.replace('M', '', 1)
            elif char == 'D':
                num += 500
                roman_num = roman_num.replace('D', '', 1)
            elif char == 'C':
                num += 100
                roman_num = roman_num.replace('C', '', 1)
            elif char == 'L':
                num += 50
                roman_num = roman_num.replace('L', '', 1)
            elif char == 'X':
                num += 10
                roman_num = roman_num.replace('X', '', 1)
            elif char == 'V':
                num += 5
                roman_num = roman_num.replace('V', '', 1)
            elif char == 'I':
                num += 1
                roman_num = roman_num.replace('I', '', 1)

        return num
