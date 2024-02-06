import random
print("Welcome to my Guessing game!")
userplaying = input("Would you like to play? ")
if userplaying.lower() == "yes":
        print("Okay, Let's Go!!")
        
user_guess = input("Make a guess? ")
if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess <= 0:
                print("Please type a number above 0")
else:
        print("Please type in a number")

random_number = random.randrange(1,4)
print(random_number)

if user_guess == random_number:
        print("You won in your first trial!")
else:
        print("Try again :)")
while True:
        NewGuess = input("Make another Guess here __" )
        if NewGuess.isdigit():
                NewGuess = int(NewGuess)
                if NewGuess <= 0:
                        print("Please type in a number above 0")
                        continue
                print(random_number)
        else:
                print("Please type in a number and not a letter!")
        if NewGuess == random_number:
                print("You matched the numbers! Congrats")
                break
        else:
                continue 