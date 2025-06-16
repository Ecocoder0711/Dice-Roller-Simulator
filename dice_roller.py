import random
# Function to Simulate Dice Roll
def simulate_Dice_Roll():
    return random.randint(1,6)
print("🎲 Welcome to the Dice Roller Simulator!")
def main():
        while True:
            dice_Number=simulate_Dice_Roll()
            input("To Roll the dice please enter.....🎲")
            print(f"🎯 you rolled a {dice_Number}")
            ask_again=input("Roll again? (y/n): ")
            if ask_again != "y" :
                print("👋 Thanks for playing! Goodbye!")
                break
if __name__== "__main__":
    main()