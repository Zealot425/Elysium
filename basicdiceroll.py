import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print("You rolled:", result)
        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

# From Chat GPT

# This program imports the random module to generate random numbers. 
# 
# The roll_dice() function uses random.randint(1, 6) to simulate rolling a six-sided die.

# In the main() function:

# It displays a welcome message.
# Enters a loop where the user can roll the dice by pressing Enter.
# It prints the result of the roll.
# Asks if the user wants to roll again. If the input is not 'y', the loop breaks, and the program ends.
# You can run this script, and it will continuously prompt you to roll the dice until you choose to exit by typing 'n'.