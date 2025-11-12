try:
    age=int(input("Enter your age"))

except ValueError as ve:
    print("Enter the number only")

finally:
    print("Exception completed")

    