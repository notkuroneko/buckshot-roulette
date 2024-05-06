import random
import math
import numpy
import time

print("Welcome to Buckshot Roulette.")
time.sleep(1)

lives = random.randint(2,5)
print("You have " + str(lives) + " lives.\n")
player = lives
dealer = lives
time.sleep(1)

def load():
    shells = random.randint(2,8)
    live = random.randint(math.trunc(shells/4)+1,shells-1-math.trunc(shells/4))
    print(str(shells) + " shells, " + str(live) + " live rounds, " + str(shells - live) + " empty.\n")
    shotgun = numpy.zeros(shells)
    for i in shotgun:
        i = bool(i)
    while live!=0:
        temp = random.randint(0,shells-1)
        if not shotgun[temp]:
            shotgun[temp] = True
            live-=1
    time.sleep(1)
    return shotgun

def shoot(shotgun, entity, count):
    if shotgun[count]:
        print("The round is live.")
        time.sleep(1)
        print("Remaining lives: " + str(entity-1) + "\n")
        return entity - 1
    else:
        print("The round is blank.")
        time.sleep(1)
        print("Remaining lives: " + str(entity) + "\n")
        return entity

sussy = 0
count = 0
shells = 0
yourTurn = True
while dealer and player:
    if count == shells:
        time.sleep(1)
        shotgun = load()
        shells = len(shotgun)
        count = 0
    if yourTurn:
        print("Choose. 0 to shoot yourself, 1 to shoot the dealer.")
        action = input()
        if action == "0":
            player = shoot(shotgun,player,count)
            if not shotgun[count]:
                yourTurn = not yourTurn
        elif action == "1":
            dealer = shoot(shotgun,dealer,count)
        else:
            print("Invalid action, please re-enter.")
            continue
    else:
        time.sleep(1)
        sussy = random.randint(0,1)
        if sussy == 0:
            print("Dealer choose: Shoot self.")
            time.sleep(1)
            dealer = shoot(shotgun,dealer,count)
            if not shotgun[count]:
                yourTurn = not yourTurn
        else:
            print("Dealer choose: Shoot YOU.")
            time.sleep(1)
            player = shoot(shotgun,player,count)
    yourTurn = not yourTurn
    count+=1

if not player:
    print("You lost, get fucked :>")
elif not dealer:
    print("You win, lucky monky :>")