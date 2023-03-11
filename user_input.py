# Getting data from the user
def get_data(MAX_PROPERTY = 5):
    data = []
    for i in range(MAX_PROPERTY):
        product_property = input(
            "Please enter quality's name, or type \"End\" to finish (Example: color): ")
        product_property = str(product_property)
        product_property = product_property.lower()
        if product_property == "end":
            break
        values = input("Please enter the values (Seperate by ','): ")
        if values:
            values = values.split(",")
        temp = {'name': product_property, 'value': values}
        data.append(temp)
    return data