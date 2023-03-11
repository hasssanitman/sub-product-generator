def column_method(thelist):
    import calculator
    # Variables
    where = 0
    the_result = []
    # Count the number of qualities
    calculated = calculator.calc_total_qualities(thelist)
    total_number_of_quality = calculated['total']
    last_qulity_counter = total_number_of_quality

    # Create all records
    for i in range(total_number_of_quality):
        the_result.append([])

    for quality in thelist:
        vals = quality['value']
        if len(vals) > 0:
            counter = int(last_qulity_counter / len(vals))
            round_of_game = total_number_of_quality / \
                int((counter * len(vals)))

            while round_of_game > 0:
                for element in vals:
                    for k in range(counter):
                        the_result[where].append(element)
                        where += 1
                round_of_game -= 1
                
            last_qulity_counter = counter
            where = 0
    return the_result
