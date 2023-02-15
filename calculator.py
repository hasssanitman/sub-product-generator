def calc_total_qualities(thelist):
    total_number_of_quality = 1
    qualities_number = []
    if len(thelist) > 0:
        for index in range(len(thelist)):
            total_number_of_quality = total_number_of_quality * \
                len(thelist[index]['value'])
            qualities_number.append(len(thelist[index]['value']))
    return {'total': total_number_of_quality, 'qualities_number': qualities_number}


def calc_qualities_counter(qualities_number, total_number_of_quality):
    if len(qualities_number) > 0:
        qualities_counter = []
        for i in range(len(qualities_number)):
            qualities_counter.append(
                int(total_number_of_quality / qualities_number[i]))
    return qualities_counter
