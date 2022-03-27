#game_7
#pile_of_coins

import random
coins = random.randint(50, 500)
print(coins)

while True:
    for player in [1, 2]:
        if player == 1:
            print("player 1: ")
            inp = int(input("enter coins number "))
            square_root = inp ** 0.5
            modulus_1 = square_root % 1
            while (modulus_1 != 0) or (inp > (coins - 1)):
                inp = int(input("enter correct coins number "))
                square_root = inp ** 0.5
                modulus_1 = square_root % 1
            coins = coins - inp
            if coins == 1:
                print("player 2 win")
                exit()
            print(coins)
        if player == 2:
            print("player 2: ")
            inp = int(input("enter coins number "))

            square_root = inp ** 0.5
            modulus_12 = square_root % 1
            while (modulus_12 != 0) or (inp > (coins - 1)):
                inp = int(input("enter correct coins number "))
                square_root = inp ** 0.5
                modulus_12 = square_root % 1
            coins = coins - inp
            if coins == 1:
                print("player 1 win")
                exit()
            print(coins)