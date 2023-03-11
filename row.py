def row_method(user_data):
    import calculator

    # Variables
    result = []
    calculated = calculator.total_sub_products(user_data)
    total_sub_products = calculated['total']
    len_of_values = calculated['len_of_values']

    counters = calculator.array_of_counters(
        len_of_values, total_sub_products)

    for i in range(total_sub_products):
        temp_array = []

        for index, prop in enumerate(counters):
            values = user_data[index]['value']
            if len(values):
                temp_array.append(values[prop['pointer']])

                if prop['amount'] != prop['a_counter'] + 1:
                    prop['a_counter'] = prop['a_counter'] + 1
                else:
                    prop['a_counter'] = 0
                    prop['pointer'] = prop['pointer'] + 1

                if prop['pointer'] == prop['lenght']:
                    prop['a_counter'] = 0
                    prop['pointer'] = 0

        result.append(temp_array)

    return result
