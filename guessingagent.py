low=1
high=100
attempts=0

print("Think of a number between 1 and 100." )

while low <= high:
    guess =(low+high)//2
    attempts +=1

    print("My guess is ", guess)
    feedback= input("Enter h (higher), l (lower), or c (correct): ").lower()

    if feedback =="c":
        print("I guessed the number!")
        print("Attempts", attempts)
        break

    elif feedback =="h":
        low= guess +1

    elif feedback== "l":
        high=guess -1

    else:
        print("Invalid input,Try again.")

else:
    print("Your feedback is inconsistent.")