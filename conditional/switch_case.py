# Here's basic example of if-elif-else statement in Python:
day = input("Enter the day of the week: ").capitalize()

if day == "Saturday" or day == "Sunday": 
    print(f"Day {day} is Weekend")
elif day == "Monday":
    print(f"Day {day} is Weekday")
elif day == "Tuesday":
    print(f"Day {day} is Weekday")
elif day == "Wednesday":
    print(f"Day {day} is Weekday")
elif day == "Thursday":
    print(f"Day {day} is Weekday")
elif day == "Friday":
    print(f"Day {day} is Weekday")
else:
    print("Invalid Day")

# The basic syntax of Match case in Python
match day:
    case "Saturday" | "Sunday":
        print(f"Day {day} is Weekend") # match weekend  
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"Day {day} is Weekday") # match weekday
    case _:
        print("Invalid Day") # Default case