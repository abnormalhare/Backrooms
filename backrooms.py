import random
import os
import time

def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

levelNum = 0

def death(reason):
    global levelNum
    clear()
    print(f"You died by {reason}")
    x = input("Play again? (Y/N)")
    x = x.lower()
    if x == "y":
        levelNum = 0
    elif x == "n":
        quit()
    else:
        death(reason)

def level(num):
    global levelNum
    checkTime = time.time()
    sel = input(f"Level {levelNum}: ")

    if sel == "select":
        levelNum = sel
    if num == "select":
        levelNum = sel

    if num == 0:
        if sel == "walk":
            ranInt = random.randint(1, 27)
            if ranInt >= 19:
                levelNum = 1
            elif ranInt == 1:
                levelNum = "Manila Room"
            elif ranInt == 2 or ranInt == 5:
                levelNum = "0!, \"White Light\""
        elif sel == "noclip":
            levelNum = -1
        elif sel == "open burnt door":
            levelNum = 0.03
        elif sel == "enter 2d houses":
            levelNum = 0.032
        elif sel == "noclip through teddy bear":
            levelNum = 0.034
        elif sel == "open childhood door":
            levelNum = 0.033
        elif sel == "stop vent":
            levelNum = 0.1
        elif sel == "break floor":
            levelNum = 27

    # Entrences: 
    # No-clipping in a bright area of Level 0.7
    elif num == "0!, \"White Light\"":
        if sel == "walk":
            ranInt = random.randint(1, 10)
            if ranInt > 7:
                levelNum = "0!, \"Red Light\""
        elif sel == "walk back":
            levelNum == 0
    
    elif num == "0!, \"Red Light\"":
        if sel == "walk":
            ranInt = random.randint(1, 20)
            if ranInt > 14:
                levelNum = "0!, \"Black Light\""
            elif ranInt < 5:
                death("an entity")
        elif sel == "walk back":
            ranInt = random.randint(1, 20)
            if ranInt > 9:
                levelNum = "0!, \"White Light\""
            elif ranInt < 3:
                death("an entity")
        elif sel == "noclip":
            ranInt = random.randint(1, 10)
            if ranInt == 5:
                levelNum = 3999
            elif ranInt == 10:
                levelNum = "The End"
            elif ranInt == 1:
                death("an entity")
    
    elif num == "0!, \"Black Light\"":
        if sel == "walk back":
            ranInt = random.randint(1, 20)
            if ranInt > 15:
                levelNum = "0!, \"White Light\""
            elif ranInt < 10:
                death("an entity")

    elif num == 0.03:
        if sel == "open moldy door":
            ranInt = random.randint(1, 8)
            if ranInt == 3:
                levelNum = 0.032
            elif ranInt > 5:
                death("an entity")
        elif sel == "open burnt door":
            ranInt = random.randint(1, 8)
            if ranInt == 4:
                levelNum = 0.034
            elif ranInt > 5:
                death("an entity")
        elif sel == "open childhood door":
            ranInt = random.randint(1, 8)
            if ranInt == 5:
                levelNum = 0.033
            elif ranInt > 5:
                death("an entity")
    
    elif num == 0.032:
        if sel == "open garage door":
            ranInt = random.randint(1, 8)
            if ranInt == 3:
                levelNum = 9
            elif ranInt > 5:
                death("an entity")
    
    elif num == 0.033:
        checkTime2 = time.time()
        if checkTime2 - checkTime > 5:
            death("psychological damage")
        if sel == "noclip under bed":
            levelNum = 11

    elif num == 0.034:
        checkTime2 = time.time()
        if checkTime2 - checkTime > 5:
            death("the teddy bear's toxic fumes")
        if sel == "enter mirror":
            levelNum = 0

    elif num == 0.1:
        if sel == "walk":
            ranInt = random.randint(1, 20)
            if ranInt == 1:
                levelNum = 1.5
            elif ranInt == 2:
                levelNum = 2.9
            elif ranInt == 3:
                levelNum = 6.5
            elif ranInt >= 10:
                death("an entity")
        elif sel == "enter black door in hallway":
            levelNum = 0.7
        elif sel == "enter restart door":
            levelNum = "0!, \"White Light\""
    
    else:
        print("You win!")
        x = input("Play again? (Y/N)")
        x = x.lower()
        if x == "y":
            levelNum = 0
        elif x == "n":
            quit()

while True:
    clear()
    level(levelNum)