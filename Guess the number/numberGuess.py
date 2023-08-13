import random

welcome = "Welcome to Guess the Number Game"
print(welcome.center(75))

x = input("Enter a number: ")

if x.isdigit():
    x = int(x)

    if x < 0:
        print("Please type a number which is 0 or above in integer.")
        quit()
else:
    print("Invalid input! Please try again.")
    quit()

y = random.randint(0, x)

guess = 0
score = 0

while True:
    guess += 1
    z = input("Make a guess: ")

    if z.isdigit():
        z = int(z)
    else:
        print('Please type a number next time.')
        continue

    if z == y:
        print("You got it!")
        score = 100 if guess <= 10 else (50 if guess <= 50 else (10 if guess <= 100 else 0))
        break
    elif z > y:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guess, "guesses")
print("Your score is", score)
