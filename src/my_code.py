#############################
# Collaborators & Sources: (enter people or resources who/that helped you)
# my family played and tested the game along with Brennan, Alex, Penelope, Nico, and Rodger
# https://www.datacamp.com/tutorial/python-arrays helped me with arrays. I just needed the syntax I already
# knew how to use arrays from robotics coding training
#############################
import random


# Write code here:
def calculate(x, y):
    if x == 1:
        return (5 + 5 * y) - 5
    else:
        return (10 + 10 * y) - 10


game_playing = input("would you like to play pigeon simulator ")
money = 0
inventory = [0, 0, 0]
while game_playing == "pigeon simulator" or game_playing == "yes":  # repeats the things below until you win or quit
    fate = input("do you want to beg for crumbs, sell things, buy things, steal bread, steal a pizza or end game ")
    chance = random.randint(1, 100)  # used to give a random number and used for all the money making techniques
    beg_money = random.randint(1, 10)   # the next 2 lines give a random amount of money every time you win money
    bank_money = random.randint(1000, 1500)
    steal_money = random.randint(10, 30)
    donuts = inventory[0]
    if fate == "beg for crumbs" or fate == "beg":  # gives the user either 1-10 crumbs or nothing
        if 40 < chance <= 100:
            print(f"you earned {beg_money} crumbs")
            money += beg_money
            print(f"you have {money} crumbs")
        elif 1 <= chance < 40:
            print("you didn't get any crumbs")
            print(f"you have {money} crumbs")
    if fate == "buy things" or fate == "buy":  # this is the shop where you can buy upgrades
        shop = input("would you like to buy a baguette(might sell for a higher value) for 5 crumbs, "
                     "a human costume(increases\n "
                     "the chances to steal a pizza) for 300 crumbs, beak extension(increases the chance of stealing \n"
                     "bread) for 100 crumbs or a bakery(win the game) for 3,000 crumbs ")
        if shop == "baguette":
            amount = int(input("how many baguettes do you want? "))
            if money >= 5 * amount:
                inventory[0] += amount
                print(f"you have bought {amount} baguettes")
                money -= 5 * amount
                print(f"you have {money} crumbs")
            else:
                print("you don't have enough crumbs")
        elif shop == "human costume":
            if money >= 300:
                inventory[1] += 1
                print("you bought a human costume")
                money -= 300
                print(f"you have {money} crumbs")
            else:
                print("you don't have enough crumbs")
        elif shop == "beak extension":
            if money >= 100:
                inventory[2] += 1
                print("you bought a beak extension")
                money -= 100
                print(f"you have {money} crumbs")
            else:
                print("you don't have enough crumbs")
        elif shop == "bakery" or "a bakery":
            if money >= 3000:
                for i in range(3):
                    if i == 0:
                        print("you won, you now have an easy way to get bread!")
                    elif i == 1:
                        print("your so cool!")
                    elif i == 2:
                        print("your such a gamer!")
                break
            else:
                print("you don't have enough crumbs")
    if fate == "steal a pizza":  # high chance to lose all crumbs high reward upgrade increases chances
        if money > 0:
            if inventory[1] > 0:
                if chance >= 50:
                    print(f"you successfully stole a pizza and earned {bank_money} crumbs")
                    money += bank_money
                    print(f"you have {money} crumbs")
                else:
                    print("you got caught and lost all your crumbs")
                    money -= money
                    print("you have 0 crumbs")
            else:
                if chance >= 95:
                    print(f"you successfully stole a pizza and earned {bank_money} crumbs")
                    money += bank_money
                    print(f"you have {money} crumbs")
                else:
                    print("you got caught and lost all your crumbs")
                    money -= money
                    print("you have 0 crumbs")
        else:
            if inventory[1] > 0:
                if chance >= 50:
                    print(f"you successfully stole a pizza and earned {bank_money} crumbs")
                    money += bank_money
                    print(f"you have {money} crumbs")
                else:
                    print("you got caught and lost all your crumbs")
                    money -= money
                    print("you have 0 crumbs")
            else:
                if chance >= 95:
                    print(f"you successfully stole a pizza and earned {bank_money} crumbs")
                    money += bank_money
                    print(f"you have {money} crumbs")
                else:
                    print("you got caught and got fined for your crime")
                    money -= 200
                    print(f"you have {money} crumbs")
    if fate == "steal bread" or fate == "bread":  # low chance to lose all crumbs, high chance to get crumbs/N/A
        if inventory[2] == 0:
            if 1 <= chance <= 10:
                print("you got caught and lost all your crumbs")
                money -= money
                print("you have 0 crumbs")
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
                print("you have 0 crumbs")
            elif 3 < chance <= 35:
                print("you got caught before you could steal the bread but you got away.")
            else:
                print(f"you earned {steal_money} crumbs")
                money += steal_money
                print(f"you have {money} crumbs")
    if fate == "sell" or fate == "sell things":  # lets you sell baguettes
        answer = input("would you like to sell baguettes ")
        if answer == "baguettes" or answer == "baguette" or answer == "yes":
            if inventory[0] > 0:
                sold = int(input("how many would you like to sell "))
                if sold > donuts:
                    print(f"you only have {inventory[0]} baguettes")
                else:
                    print("You: would you like to buy my baguette")
                    haggle = int(input("Random pigeon: how many crumbs? "))
                    if haggle <= calculate(1, sold):
                        print("Random pigeon: sure")
                        money += haggle
                        inventory[0] -= sold
                        print(f"you have {money} crumbs")
                    elif haggle <= calculate(2, sold):
                        if chance < 50:
                            print("Random pigeon: that's a bit steep but ok")
                            money += haggle
                            inventory[0] -= sold
                            print(f"you have {money} crumbs")
                        else:
                            print("Random pigeon: no way that is a crazy expensive baguette")
                    else:
                        if chance > 99:
                            print("Random pigeon:I don't have anything else to buy so I will take it")
                            money += haggle
                            inventory[0] -= sold
                            print(f"you have {money} crumbs")
                        else:
                            print("Random pigeon: you must be nuts charging that price for a baguette")
            else:
                print("you don't have any baguettes")
        else:
            print("that is not an option")
    if fate == "end game":
        break
