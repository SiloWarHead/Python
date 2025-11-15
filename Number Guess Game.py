import random

diff = input("Choose difficulty(easy/moderate/hard): ")
if diff == "easy":
    n = random.randint(1,10)
    print("Guess between 1-10\n")
elif diff == "moderate":
    n = random.randint(1,20)
    print("Guess between 1-20\n")
elif diff == "hard":
    n = random.randint(1,30)
    print("Guess between 1-30\n")

wrong = 0

for i in range(3):
    guess = int(input("Your guess: "))

    if guess > n:
        wrong += 1
        print("Too Large\n")
    elif guess < n:
        wrong += 1
        print("Too Small\n")
    else:
        print("Congrats! You have won!")
        break

if wrong == 3:
    print("Game Over")
    print("Correct was: ", n)
