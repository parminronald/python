"""  string operation in python
    len()       # to get the length of the string
    count()     # to count the string
    lower()     # to convert the string to lower case
    upper()     # to convert the string to upper case
    capitalize()    # to convert the string to capitalize case
    title()     # to convert the string to title case   
    find()      # to find the string
    replace()   # to replace the string
    split()     # to split the string
    strip()     # to remove the white space
    isdigit()   # to check if the string is digit
    isalpha()   # to check if the string is alphabet
    isalnum()   # to check if the string is alphanumeric
    isspace()   # to check if the string is space
    startswith()# to check if the string is start with
    endswith()  # to check if the string is end with
    join()      # to join the string
    format()    # to format the string
    splitlines()# to split the string by line
    center()    # to center the string
    ljust()     # to left justify the string
    rjust()     # to right justify the string
"""
# example of string operation
name = "python is a programming language"
name_length = len(name)
name_count = name.count("a") # count the character "a" in the string
name_lower = name.lower()
name_upper = name.upper()
name_capitalize = name.capitalize() # capitalize the first character of the string
name_title = name.title() # capitalize the first character of each word in the string
print(f"Length of Name is {name_length}")
print(f"Count of Name is {name_count}") 
print(f"Lower of Name is {name_lower}")
print(f"Upper of Name is {name_upper}")
print(f"Capitalize of Name is {name_capitalize}")
print(f"Title of Name is {name_title}")
