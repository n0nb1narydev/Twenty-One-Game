from random import choice
from time import sleep
from os

CHOICES = [1, 2, 3]
playing = True

def player_turn():
    global total
    global game_over
    num = 0

    while num not in CHOICES:
        try:
            num = int(input("Choose a number between 1 and 3: "))
        except ValueError:
            print("Invalid Entry.")

    total += num
    if total == 21:
        print("You have won! You got the sum to 21!")
        game_over = True
    elif total > 21:
        print("*Sad Trombone* You busted!")
        game_over = True
    else:
        print(f"The total is now: {total}")

def ai_turn():
    global total
    global game_over

    if total == 18:
        num = 3
        total += num
    elif total == 19:
        num = 2
        total += num
    elif total == 20:
        num = 1
        total += num
    else:
        num = choice(CHOICES)
        total += num

    print(f"The computer has chosen: {num}")
    sleep(1)
    if total == 21:
        print("You have lost. The computer got the sum to 21!")
        game_over = True
    else:
        print(f"The total is now: {total}")


def play_again():
    while True:
        again = input("Would you like to play again? (yes/no) ").lower()
        if again == 'yes':
            return True
        elif again == 'no':
            print("Thanks for playing! Come back again soon.")
            return False
        else:
            continue


def clear():
    if name ==

while playing:
    print("Let's Play 21!\nGet the running total to 21 before the computer does!")
    sleep(2)
    total = 0
    game_over = False
    while total < 21:
        player_turn()
        sleep(1)
        if game_over:
            break
        ai_turn()
        sleep(1)
        if game_over:
            break
    playing = play_again()

