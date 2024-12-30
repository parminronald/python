# Here's basic example of if-elif-else statement in Python:
day = input("Enter the day of the week: ").capitalize()

if day == "Saturday" or day == "Sunday": 
    print(f"Day {day} is Weekend")
elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] :
    print(f"Day {day} is Weekday")
else:
    print("That's not valid day of the week")

# The basic syntax of Match case in Python
match day:
    case "Saturday" | "Sunday":
        print(f"Day {day} is Weekend") # match weekend  
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"Day {day} is Weekday") # match weekday
    case _:
        print("That's not valid day of the week") # Default case

# Example: Handling HTTP methods in a Flask-like application
method = "POST"

match method:
    case "GET":
        print("Fetching resource...")
    case "POST":
        print("Creating resource...")
    case "PUT":
        print("Updating resource...")
    case "DELETE":
        print("Deleting resource...")
    case _:
        print("Unsupported HTTP method.")

# Example: API response status code handling
status_code = 200

match status_code:
    case 200:
        print("Request succeeded.")
    case 404:
        print("Resource not found.")
    case 500:
        print("Server error. Please try again later.")
    case _:
        print("Unknown status code.")

# Example: Categorizing configurations
config = {"type": "database", "name": "PostgreSQL", "version": 13}

match config:
    case {"type": "database", "name": name, "version": version}:
        print(f"Database: {name} (Version {version})")
    case {"type": "cache", "name": name}:
        print(f"Cache system: {name}")
    case _:
        print("Unknown configuration.")
