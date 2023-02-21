def calc_total_qualities(thelist):
    total_number_of_quality = 1
    len_of_items = []

    if len(thelist) > 0:
        for index in range(len(thelist)):
            item_len = len(thelist[index]['value'])
            total_number_of_quality = total_number_of_quality * item_len
            len_of_items.append(item_len)

    return {'total': total_number_of_quality, 'len_of_items': len_of_items}


def calc_the_counter(len_of_items, total_number_of_quality):
    if len(len_of_items) > 0:
        latest = total_number_of_quality
        the_counter = []

        for i in range(len(len_of_items)):
            temp = {'c': 0, 'c_p': 0, 'p': 0, 'len': 0}
            temp['c'] = int(latest / len_of_items[i])
            temp['len'] = len_of_items[i]
            the_counter.append(temp)

            latest = temp['c']

        return the_counter