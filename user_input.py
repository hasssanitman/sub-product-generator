# Getting data from the user
def get_data(MAX_QUALITY = 5):
    theList = []
    for i in range(MAX_QUALITY):
        quality_input = input(
            "Please enter quality's name, or type \"End\" to finish (Example: color): ")
        quality_input = str(quality_input)
        quality_input = quality_input.lower()
        if quality_input == "end":
            break
        value_input = input("Please enter the values (Seperate by ','): ")
        if value_input:
            value_input = value_input.split(",")
        temp = {'name': quality_input, 'value': value_input}
        theList.append(temp)
    return theList