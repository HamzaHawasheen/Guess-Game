import random
import time
print("Hello")
time.sleep(1)
print("This is game of Guess a number")
time.sleep(1)
print("""Play Steps: 
         1. Set boundaries by which you want to guess the generated number
         2. Insert the number you expect (just integer)
         3. You have 5 tries
         4. Good Luck""")
time.sleep(1)
def Generation_and_Guesss():
    print("Please enter the period limits you wants: ")
    period_limit1 = int(input())
    period_limit2 = int(input())
    if period_limit2 > period_limit1:
        number_Generation = random.randrange(period_limit1,period_limit2)
        print("What is your guess of the number that will appear")
        number_Guess = int(input())
        tries = 1
        while number_Guess != number_Generation:
            print("Your answer is Wrong! Please try again")
            print("What is your guess of the number that will appear")
            number_Guess = int(input())
            tries += 1
            if tries == 5:
                print("Your tries is finished! Game Over! ")
                break
        if number_Guess == number_Generation:
            print("Excellent! Your answer is correct")
    else:
        print("The second term must be greater than the first term")
Generation_and_Guesss()