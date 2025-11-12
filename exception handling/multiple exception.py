try:
    age=int(input("Enter your age "))
    age = age/0

except ValueError as ve:
    print("Enter the number only")
except ZeroDivisionError as ex:
    print("Number cannot be divided by zero")

else:
    print("No exceptions")

finally:
    print("Exception completed")
