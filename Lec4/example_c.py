# Синтаксис одиночного условного оператора
# if expression:
#     body

age = int(input())

if age >= 18:
    print("Your age is:", age)
    print("Welcome to our service!")
    print("Press here to continue!")
    if age >= 25:
        print("You are very old")
        if age >= 37:
            print("You are super old!")
    
print("Service done!")