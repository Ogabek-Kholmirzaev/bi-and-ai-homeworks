import random

while True:
    rand = random.randint(1,100)
    attempts = 0
    is_found = False

    while True:
        number = int(input())

        attempts += 1

        if number == rand:
            is_found = True
            break
        elif number > rand:
            print("Too high!")
        else:
            print("Too low!")

        if attempts == 10:
            break

    if is_found:
        print("You guessed it right!")
        break
    else:
        print("You lost, you have attempted 10 times. Want to play again? If yes, type Y/YES/yes/ok")

        is_want_play = input()

        if is_want_play == "Y" or "YES" or 'y' or 'yes' or 'ok':
            continue
        else:
            print("Thank you for playing!")
            break