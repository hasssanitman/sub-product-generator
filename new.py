def new_method(thelist):
    import calculator

    # Variables
    the_result = []
    calculated = calculator.calc_total_qualities(thelist)
    total_number_of_quality = calculated['total']

    # c => counter
    # p => pointer
    # c_p => counter pointer
    # len => length qualifies
    the_counter = calculator.calc_the_counter(
        calculated['len_of_items'], total_number_of_quality)
    print(the_counter)
    for i in range(total_number_of_quality):
        temp_array = []

        for index, val in enumerate(the_counter):
            vals = thelist[index]['value']
            if len(vals):
                temp_array.append(vals[val['p']])

                if val['c'] != val['c_p'] + 1:
                    val['c_p'] = val['c_p'] + 1
                else:
                    val['c_p'] = 0
                    val['p'] = val['p'] + 1

                if val['p'] == val['len']:
                    val['c_p'] = 0
                    val['p'] = 0

        the_result.append(temp_array)

    return the_result
