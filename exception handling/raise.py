try:
    age=int(input("enter the age for the driving license "))

    if age<18:
        raise ValueError
    else:
        print("Eligible for driving license")


except ValueError as ve:
    print("Not eligible for driving license")