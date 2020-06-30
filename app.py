menu = """Please select one of the folowwing options:
1) Add new entry for today
2) View entries
3) Exit

Your selection: """

welcome = "Welcome to the programming jourmal"

print(welcome)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        print("adding")
    elif user_input == "2":
        print("view")
    else:
        print("Invalid option, please try again!")
