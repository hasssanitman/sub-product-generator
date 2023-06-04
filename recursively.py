result = []
data = []

def rec_method(user_data, idx):
    global data
    data = user_data
    return recursively(idx, [])


def recursively(idx, temp_array):
    for property in data[idx]["value"]:
        if idx == 0:
            temp_array = []
        if idx+1 < len(data):
            temp = temp_array.copy()
            temp.append(property)
            recursively(idx+1, temp)
        else:
            copy = temp_array.copy()
            copy.append(property)
            result.append(copy)

    return result
