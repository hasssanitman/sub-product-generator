def new_method(thelist):
    import calculator
    # Variables
    total_number_of_quality = 1
    qualities_number = []
    qualities_counter = []

    # Count the number of qualities
    calculated = calculator.calc_total_qualities(thelist)
    total_number_of_quality = calculated['total']
    qualities_number = calculated['qualities_number']

    # Count each qualities how many need to print
    qualities_counter = calculator.calc_qualities_counter(
        qualities_number, total_number_of_quality)

    print(total_number_of_quality)
    print(qualities_number)
    print(qualities_counter)
# New Method
# def generate(the_list, index = 0):
#     if len(the_list[index]['value']) > 0:
#         vals = the_list[index]['value']
#         result = []
#         counter = int(total_number_of_quality / len(vals))
#         for val in vals:
#             for i in range(counter):
#                 if index < len(the_list) - 1:
#                     result.append([val, generate(the_list, index + 1)])
#                 else:
#                     result.append(val)


#         if index < len(the_list) - 1:
#             counter = int(total_number_of_quality / len(vals))
#             regenerate(vals, counter)
#             for val in vals:
#                 for i in range(counter):
#                     if index < len(the_list) - 1:
#                         result.append([val, generate(the_list, index + 1)])
#                     else:
#                         result.append(val)



    
#         return result   