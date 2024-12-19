import random

choices = ['rock', 'paper', 'scissor']

for index, choice in enumerate(choices):
    print(index, choice)

cnt_player = 0
cnt_computer = 0

while True:
    player = -1
    computer = random.randint(0, 2)

    while True:
        player = int(input('Enter your choice: '))

        if player < 0 or player > 2:
            print('Choose a number between 0 and 2')
        else:
            break

    print('Computer choice:', computer, '\n')

    if player == 0:
        if computer == 1:
            cnt_computer += 1
        elif computer == 2:
            cnt_player += 1

    if player == 1:
        if computer == 0:
            cnt_player += 1
        elif computer == 2:
            cnt_computer += 1

    if player == 2:
        if computer == 0:
            cnt_computer += 1
        elif computer == 1:
            cnt_player += 1

    if cnt_player == 5 or cnt_computer == 5:
        break

if cnt_player == 5:
    print('You win!')
else:
    print('You lose!')