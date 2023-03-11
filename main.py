import user_input
import column
import row
import recursively

print("Welcome to the sub-product-generator script!")

# Get Data from the user
user_data = user_input.get_data(5)

method = ''

while not method.isdigit() or not method.isnumeric():
    method = input("Select the method (0 = column, 1 = row, 2 = recursive):")
    if method.isdigit() or method.isnumeric():
        pass
    else:
        print("Entered number is invalid")

method = int(method)

if method == 1:
    # Row Method
    print("Row Method")
    print(row.row_method(user_data))
elif method == 2:
    # Recursive Method
    print("Recursive Method")
    print(recursively.rec_method(user_data))
else:
    # Column Method
    print("Column Method")
    print(column.column_method(user_data))


print("END OF SCRIPT")
