names = ['Sarah', 'Fred','Mike','Aria']
hometown = ['Detroit','Ann Arbor','Sterling Heights','Grand Rapids']
favorite_food = ['sushi', 'pizza','tacos','burgers']
while True:
    student = int(input("Welcome! Which student would you like to learn more about? Enter a number 1-4: "))
    options = input("Would you like to see a list? y/n ")
    if options == "y":
        for name in names:
            print(name)
    if options == "n":
        print("Ok")
        search = input("Enter student's name: ")
        for name in names:
            if name.lower() == search.lower():
                print(f'{search} found')
            else:
                print('Student not found.')
    if student == 1:
     print(f"Student 1 is {names[0]}. What would you like to know?")
    elif student == 2:
     print(f"Student 2 is {names[1]}. What would you like to know?")
    elif student == 3:
     print(f"Student 3 is {names[2]}. What would you like to know?")
    elif student == 4:
     print(f"Student 4 is {names[3]}. What would you like to know?")
    else:
     print("Invalid number")

    category = input("Enter 'hometown' or 'favorite food'. ")
    if category.lower() == 'hometown':
        print(f'{names[student-1]} is from {hometown[student-1]}.')
    if category.lower() == 'favorite food' or 'food':
        print(f'{names[student-1]} favorite food is {favorite_food[student-1]}')
    else:
        print("That category does not exist. Please try again.")

    response = input("Would you like to learn about another student? y/n ")
    if response.lower() == "y":
        print("OK")
    if response.lower() == "n":
        print("Thanks!")
        break