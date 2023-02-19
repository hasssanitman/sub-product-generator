import user_input
import old
import new
import recursively

print("Welcome to the sub-product-generator script!")

# Get Data from the user
theList = user_input.get_data(5)

method = ''

while not method.isdigit() or not method.isnumeric():
    method = input("Select the method (0 = old, 1 = new, 2 = recursive):")
    if method.isdigit() or method.isnumeric():
        int(method)
    else:
        print("Entered number is invalid")

if method == 1:
    # New Method
    print(new.mew_method(theList))
elif method == 2:
    # Recursive Method
    print(recursively.rec_method(theList))
else:
    # Old Method
    print(old.old_method(theList))


print("END OF SCRIPT")
