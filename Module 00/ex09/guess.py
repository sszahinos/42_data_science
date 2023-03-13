from random import randint

def print_welcome():
    """This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!"""

to_guess = randint(1, 99)
tries = 0
print_welcome()
while(True):
    num = input("What's your guess between 1 and 99? ")
    if num.lower() == "exit":
        message = "Goodbye!"
        break
    if not num.isdigit():
        print("That's not a number")
    else:
        num = int(num)
        if num == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if num == to_guess:
            if tries == 0:
                message = "Congratulations! You got it on your first try!"
            else:
                message = "You won in {} attempts!".format(tries)
            break
        if num > to_guess:
            print("Too high!")
        else:
            print("Too low!")
    tries += 1
print(message)