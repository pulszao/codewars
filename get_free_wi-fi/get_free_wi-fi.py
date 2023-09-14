def nonstop_hotspot(area):
    wifi = 0
    phone_index = area.find('P')

    for index in range(phone_index - 1, -1, -1):
        if area[index] == '*':
            wifi += 1
        elif area[index] == '#':
            break

    for index in range(phone_index + 1, len(area)):
        if area[index] == '*':
            wifi += 1
        elif area[index] == '#':
            break
    return wifi


# Exemplo de uso
a = nonstop_hotspot('*   P  *   *')
print(a)
