def total_sub_products(user_data):
    total_sub_products = 1
    len_of_values = []

    if len(user_data) > 0:
        for index in range(len(user_data)):
            item_len = len(user_data[index]['value'])
            total_sub_products = total_sub_products * item_len
            len_of_values.append(item_len)

    return {'total': total_sub_products, 'len_of_values': len_of_values}


def array_of_counters(len_of_values, total_sub_products):
    if len(len_of_values) > 0:
        latest = total_sub_products
        counters = []

        for i in range(len(len_of_values)):
            temp = {'amount': 0, 'a_counter': 0, 'pointer': 0, 'lenght': 0}
            temp['amount'] = int(latest / len_of_values[i])
            temp['lenght'] = len_of_values[i]
            counters.append(temp)

            latest = temp['amount']

        return counters