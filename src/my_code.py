#############################
# Collaborators & Sources: (enter people or resources who/that helped you)
# 
#
#
#############################
import random

import numpy


# Write code here:
def lose():
    print("you have 0 crumbs")


game_playing = input("would you like to play pigeon simulator ")
money = 0
inventory = numpy.array([0, 0, 0])
while game_playing == "pigeon simulator" or "yes":
    fate = input("do you want to beg for crumbs, sell things, buy things, steal bread, steal a pizza or end game ")
    chance = random.randint(1, 100)
    beg_money = random.randint(1, 10)
    bank_money = random.randint(1000, 1500)
    steal_money = random.randint(10, 30)
    donuts = int(inventory[0])
    if fate == "beg for crumbs" or fate == "beg":
        if 50 < chance <= 100:
            print(f"you earned {beg_money} crumbs")
            money += beg_money
            print(f"you have {money} crumbs")
        elif 1 <= chance < 50:
            print("you didn't get any crumbs")
            print(f"you have {money} crumbs")
    if fate == "buy things" or fate == "buy":  # this is the shop
        shop = input("would you like to buy a baguette(might sell for a higher value) for 5 dollars, "
                     "a human costume(increases\n "
                     "the chances to steal a pizza) for 300 dollars, beak extension(increases the chance of stealing \n"
                     "bread) for 100 or a bakery(win the game) for 3,000 crumbs ")
        if shop == "baguette":
            if money >= 5:
                inventory[0] += 1
                print("you have bought a baguette")
                money -= 5
                print(f"you have {money} crumbs")
            else:
                print("you don't have enough crumbs")
        if shop == "human costume":
            if money >= 300:
                inventory[1] += 1
                print("you bought a human costume")
                money -= 300
                print(f"you have {money} crumbs")
            else:
                print("you don't have enough crumbs")
        if shop == "beak extension":
            if money >= 100:
                inventory[2] += 1
                print("you bought a beak extension")
                money -= 100
                print(f"you have {money} crumbs")
            else:
                print("you don't have enough crumbs")  # end of shop
        if shop == "bakery":
            if money >= 3000:
                print("you won, you now have an easy way to get bread!")
                break
            else:
                print("you don't have enough money")
    if fate == "steal a pizza":
        if inventory[1] > 0:
            if chance >= 50:
                print(f"you successfully stole a pizza and earned {bank_money} crumbs")
                money += bank_money
                print(f"you have {money} crumbs")
            else:
                print("you got caught and lost all your crumbs")
                money -= money
                lose()
        else:
            if chance >= 95:
                print(f"you successfully stole a pizza and earned {bank_money} crumbs")
                money += bank_money
                print(f"you have {money} crumbs")
            else:
                print("you got caught and lost all your crumbs")
                money -= money
                lose()
    if fate == "steal bread" or fate == "bread":
        if inventory[2] == 0:
            if 1 <= chance <= 10:
                print("you got caught and lost all your crumbs")
                money -= money
                lose()
            elif 10 < chance <= 50:
                print("you got caught before you could steal the bread but you got away")
            else:
                print(f"you earned {steal_money} crumbs")
                money += steal_money
                print(f"you have {money} crumbs")
        else:
            if 1 <= chance <= 3:
                print("you got caught and lost all your crumbs")
                money -= money
                lose()
            elif 3 < chance <= 35:
                print("you got caught before you could steal the bread but you got away.")
            else:
                print(f"you earned {steal_money} crumbs")
                money += steal_money
                print(f"you have {money} crumbs")
    if fate == "sell" or fate == "sell things":
        answer = input("would you like to sell baguettes ")
        if answer == "baguettes" or answer == "baguette" or answer == "yes":
            if inventory[0] > 0:
                sold = int(input("how many would you like to sell "))
                if sold > donuts:
                    print(f"you only have {inventory[0]} baguettes")
                else:
                    print("You: would you like to buy my baguette")
                    haggle = int(input("Random pigeon: how many crumbs? "))
                    if haggle <= (5 + 5 * donuts) - 5:
                        print("Random pigeon: sure")
                        money += haggle
                        print(f"you have {money} crumbs")
                    elif haggle < (10 + 5 * donuts) - 5:
                        if chance < 50:
                            print("Random pigeon: that's a bit steep but ok")
                            money += haggle
                            print(f"you have {money} crumbs")
                        else:
                            print("Random pigeon: no way that is a crazy expensive baguette")
                    else:
                        if chance > 99:
                            print("Random pigeon:I don't have anything else to buy so I will take it")
                            money += haggle
                            print(f"you have {money} crumbs")
                        else:
                            print("Random pigeon: you must be nuts charging that price for a baguette")
            else:
                print("you don't have any baguettes")
        else:
            print("that is not an option")
    if fate == "end game":
        break
