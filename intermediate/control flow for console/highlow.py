import random

numRounds = 5
score = 0

print("Welcome to the High-Low Game!")
print("--------------------------------")

for round_num in range(1, numRounds + 1):
    print(f"Round {round_num}")

    user = random.randint(1, 100)
    computer = random.randint(1, 100)

    print(f"Your number is {user}")

    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess not in ["higher", "lower"]:
        guess = input("Please enter either higher or lower: ").lower()

    if guess == "higher":
        if user < computer:
            print("You were right! The computer's number was", computer)
            score += 1  
        else:
            print("That's incorrect. The computer's number was", computer)
    elif guess == "lower":
        if user > computer:
            print("You were right! The computer's number was", computer)
            score += 1  
        else:
            print("That's incorrect. The computer's number was", computer)

    print("Your score is now", score)
    print()  

print("Thanks for playing!")
print("Your final score is:", score)
if score == numRounds:
    print("Wow! You played perfectly!")
elif score >= numRounds // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
