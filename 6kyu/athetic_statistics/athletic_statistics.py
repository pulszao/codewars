def stat(strg):
    all_datatime = []
    times = strg.replace(' ', '').split(',')

    for time in times:
        aux_time = time.split('|')
        seconds = (int(float(aux_time[0])) * 3600) + (int(float(aux_time[1]) // 1) * 60) + int(float(aux_time[2]))
        all_datatime.append(seconds)

    length = len(all_datatime)

    # Sort list
    all_datatime = sorted(all_datatime)

    # Average
    average = 0
    for data in all_datatime:
        average += data/length
    average = get_formatted_time(average)

    # Range
    lowest = min(all_datatime)
    highest = max(all_datatime)
    range = get_formatted_time(int(highest) - int(lowest))

    # Median
    median = 0
    if (length % 2) == 0:
        index = (length // 2)
        median = get_formatted_time((int(all_datatime[index]) + int(all_datatime[index - 1])) / 2)
    else:
        index = (length // 2)
        median = get_formatted_time(int(all_datatime[index]))

    return f"Range: {range} Average: {average} Median: {median}"


def get_formatted_time(seconds):
    return str(int(seconds // 3600)).zfill(2) + '|' + str(int((seconds % 3600) // 60)).zfill(2) + '|' + str(int((seconds % 3600) % 60)).zfill(2)
