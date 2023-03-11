def column_method(user_data):
    import calculator
    # Variables
    index = 0
    result = []
    # Count the number of qualities
    calculated = calculator.total_sub_products(user_data)
    total_sub_products = calculated['total']
    last_property_counter = total_sub_products

    # Create all records
    for i in range(total_sub_products):
        result.append([])

    for prop in user_data:
        values = prop['value']
        if len(values) > 0:
            counter = int(last_property_counter / len(values))
            round_of_game = total_sub_products / \
                int((counter * len(values)))

            while round_of_game > 0:
                for element in values:
                    for k in range(counter):
                        result[index].append(element)
                        index += 1
                round_of_game -= 1
                
            last_property_counter = counter
            index = 0
    return result
