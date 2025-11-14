import random
playing=True



print("I will generate numbers between 1 to 10. Guess the number ")


while playing:
    number=random.randint(1,10)
    guess=int(input("Enter your number"))
    if guess==number:
        print("Correct guess" )
        print("The number was ",number)
        playing=False
        break

    else:
        print("Wrong guess,Try again")
        print("The number was ",number)
        
        