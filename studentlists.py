names = ['Sarah', 'Fred','Mike','Aria']
hometown = ['Detroit','Ann Arbor','Sterling Heights','Grand Rapids']
favorite_food = ['sushi', 'pizza','tacos','burgers']
while True:
    student = input("Welcome! Which student would you like to learn more about? Would you like to enter a number 1-4? y/n: ")
    if student == "y":
        student_choice = int(input("Enter a number 1-4: "))
        if student_choice == 1:
            print(f"Student 1 is {names[0]}. What would you like to know?")
        elif student_choice == 2:
            print(f"Student 2 is {names[1]}. What would you like to know?")
        elif student_choice == 3:
            print(f"Student 3 is {names[2]}. What would you like to know?")
        elif student_choice == 4:
            print(f"Student 4 is {names[3]}. What would you like to know?")
        else:
            print("Invalid number")
        category = input("Enter 'hometown' or 'favorite food'. ")
        if category.lower() == 'hometown':
            print(f'{names[student_choice - 1]} is from {hometown[student_choice - 1]}.')
        elif category.lower() == 'favorite food' or category.lower() == 'food':
            print(f'{names[student_choice - 1]} favorite food is {favorite_food[student_choice - 1]}')
        else:
            print("That category does not exist. Please try again.")
    if student == "n":
        options = input("Would you like to see a list? y/n ")
        if options == "y":
            for name in names:
             print(name)
        elif options == "n":
            print("Ok")
        search_question = input("Would you like to search a student's name? yes/no ")
        if search_question == "yes":
            search = input("Enter student's name: ")
            for name in names:
             if name.lower() == search.lower():
                print(f'{search.lower()} found')
                category = input("Enter 'hometown' or 'favorite food'. ")
                if category == "hometown":
                    print(f"{search}'s hometown is {hometown[names.index(name)]}.")
                if category == "favorite food":
                        print(f"{search}'s favorite food is {favorite_food[names.index(name)]}")
                break
             else:
                print('Student not found.')
        elif search_question =="no":
            print("Thank you.")

    response = input("Would you like to learn about another student? y/n ")
    if response.lower() == "y":
        print("OK")
    if response.lower() == "n":
        print("Thanks!")
        break