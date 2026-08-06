import random

# -1 = Snake, 0 = Water, 1 = Gun
computer = random.choice([-1, 0, 1])

print("Welcome to Snake, Water, Gun Game!")
print("Choose:")
print("-1 for Snake")
print(" 0 for Water")
print(" 1 for Gun")

you = int(input("Enter your choice: "))

print("\nComputer chose:", computer)
print("You chose:", you)

if computer == you:
    print("Match Draw!")

elif (computer == -1 and you == 1):
    print("You Win!")

elif (computer == -1 and you == 0):
    print("You Lose!")

elif (computer == 1 and you == -1):
    print("You Lose!")

elif (computer == 1 and you == 0):
    print("You Win!")

elif (computer == 0 and you == -1):
    print("You Win!")

elif (computer == 0 and you == 1):
    print("You Lose!")

else:
    print("Invalid Input! Please enter only -1, 0, or 1.")