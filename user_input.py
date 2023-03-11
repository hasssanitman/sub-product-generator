# Getting data from the user
def get_data(MAX_PROPERTY = 5):
    user_data = []
    for i in range(MAX_PROPERTY):
        product_property = input(
            "Please enter property's name, or type \"Exit\" to finish (Example: color): ")
        product_property = str(product_property)
        product_property = product_property.lower()
        if product_property == "exit":
            break
        values = input("Please enter the values (Seperate by ','): ")
        if values:
            values = values.split(",")
        temp = {'name': product_property, 'value': values}
        user_data.append(temp)
    return user_data