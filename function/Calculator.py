def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def div(a,b):
    return a/b

print("Select operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter the number of the opertation"))

num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))

if choice==1:
    print(add(num1,num2))

elif choice==2:
    print(sub(num1,num2))

elif choice==3:
    print(multiply(num1,num2))
elif choice==4:
    print(div(num1,num2))

else:
    print("Invalid input")