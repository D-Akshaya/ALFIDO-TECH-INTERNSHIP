import random

def number_guessing_game():
    number_to_guess=random.randint(1,100)
    attempts=0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_guess=input("Take a guess:")

        if user_guess.lower()=="quit":
            print("okay, the number was{}.Thanks for playing!".format(number_to_guess))
            break

        try:
            user_guess=int(user_guess)
        except ValueError:
            print("That's not a valid number!")
            continue

        if user_guess<1 or user_guess>100:
            print("Please guess a number between 1 and 100.")
            continue
        attempts +=1

        if user_guess == number_to_guess:
            print(f"Congtatulations! You found he number in {attemptd} attemptd,")
            break
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
if __name__ =="__main__":
    number_guessing_game()

        

         
