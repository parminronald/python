# primitive data structure in python {string, integer, float, boolean}
# "string" is a sequence of characters exapmle: "python", "1234", "1.234" etc
# "integer" is a whole number exapmle: 1, 100, 2, 20, 3, 4 etc
# "float" is a decimal number exapmle: 1.23, 2.34, 3.45, 4.56 etc
# "boolean" is a True or False exapmle: True, False

# example of string code
name = "python"
version = "3.7.4"
print(f"My Name is {name} and version is {version}")

# string operator in python
# + operator, to combine two or more strings
# * operator, to repeat the string
# [] operator, to slice the string

# example of string operator
first_name = "Ronald"
last_name = "Suparmin"
full_name = first_name + " " + last_name
print(f"My Full Name is {full_name}")

# example of repeat string
repeat_string = "Hello Python"
repeat_string = repeat_string * 3
print(f"Repeat String is {repeat_string}")

# example of slice string
slice_string = "Hello Python"
slice_string = slice_string[0:5]    # slice string from index 0 to 5
print(f"Slice String is {slice_string}")

# example of integer code
age = 25
print(f"My name is {name}, My Age is {age}")

# example of float code
price_coffee = 1.23
buy_coffee = 2
total_price = price_coffee * buy_coffee
print(f"Price of Coffee is {price_coffee}, Buy Coffee {buy_coffee}, Total Price is {total_price}")

# example of boolean code
is_student = True
if is_student:
    print("Student")
else:    
    print("Not Student")    