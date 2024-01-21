import random

print("Welcome to the guessing Game")

lower_limit = 1
upper_limit = 100
secret_number = random.randint(lower_limit, upper_limit)

for attempt in range(1, 6):  # Allow up to 5 attempts
    print(f"Attempt {attempt}")
    
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print(f"Congratulations! You guessed the correct number {secret_number} in {attempt} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

