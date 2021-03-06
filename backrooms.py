import random
import os
import time

### Standardization ###

# random.randint(1, 10) #
# Level 1: 10 unsafe, else safe
# Level 2: > 8 unsafe, else safe
# Level 3: >= 7 unsafe, else safe
# Level 4: >= 5 unsafe, else safe

# random.randint(1, 20) #
# Level 5: <= 12 unsafe, else safe
# Level 6: <= 14 unsafe, else safe
# Level 7: <= 17 unsafe, else safe

# random.randint(1, 30) #
# Level Death: <= 26 unsafe, else safe

def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

levelNum = 0
msg = ""
playerItems = []

def win():
    global levelNum
    print("You win!")
    x = input("Play again? (Y/N)")
    x = x.lower()
    if x == "y":
        levelNum = 0
    elif x == "n":
        quit()
    else:
        win()

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

def helpRooms(tabl):
    print("try typing \"" + tabl[random.randint(0, len(tabl))] + '"')
    time.sleep(2.5)

def level(num):
    ### set variables ###
    global levelNum
    global msg
    checkTime = time.time()
    if msg != "":
        print(msg)
    msg = ""
    sel = input(f"Level {levelNum}: ")

    ### set level specific things ###
    ranLev = random.randint(1, 250)
    if ranLev == 250:
        levelNum = 0.3
    elif ranLev == 249:
        levelNum = 0.45
        msg = "You got pulled down here by a hand on the ground!"

    if sel == "use catatonia" and playerItems.count("catatonia") > 0:
        ranInt = random.randint(1, 4)
        if ranInt == 4:
            levelNum = 0.4
        else:
            levelNum = 404

    if num == 0:
        if sel == "help":
            helpRooms(["walk", "noclip", "open burnt door", "enter 2d houses", "noclip through teddy bear", "open childhood door", "enter vent", "open brown door", "break floor"])

        elif sel == "walk":
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
        elif sel == "enter vent":
            levelNum = 0.1
        elif sel == "open brown door":
            levelNum = 0.22
        elif sel == "break floor":
            levelNum = 27

    # Entrences: 
    # No-clipping in a bright area of Level 0.7
    elif num == "0!, \"White Light\"":
        if sel == "help":
            helpRooms(["walk", "walk back"])
        
        elif sel == "walk":
            ranInt = random.randint(1, 10)
            if ranInt > 7:
                levelNum = "0!, \"Red Light\""
        elif sel == "walk back":
            levelNum = 0
    
    elif num == "0!, \"Red Light\"":
        if sel == "help":
            helpRooms(["walk", "walk back", "noclip"])

        elif sel == "walk":
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
        if sel == "help":
            helpRooms(["walk back"])

        elif sel == "walk back":
            ranInt = random.randint(1, 20)
            if ranInt > 15:
                levelNum = "0!, \"Red Light\""
            elif ranInt < 10:
                death("an entity")

    elif num == 0.03:
        if sel == "help":
            helpRooms(["open moldy door", "open burnt door", "open childhood door"])

        elif sel == "open moldy door":
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
        if sel == "help":
            helpRooms(["open garage door"])

        elif sel == "open garage door":
            ranInt = random.randint(1, 8)
            if ranInt == 3:
                levelNum = 9
            elif ranInt > 5:
                death("an entity")
    
    elif num == 0.033:
        checkTime2 = time.time()
        if checkTime2 - checkTime > 5:
            death("psychological damage")
            
        if sel == "help":
            helpRooms(["noclip under bed"])

        elif sel == "noclip under bed":
            levelNum = 11

    elif num == 0.034:
        checkTime2 = time.time()
        if checkTime2 - checkTime > 5:
            death("the teddy bear's toxic fumes")
        
        if sel == "help":
            helpRooms(["enter mirror"])

        elif sel == "enter mirror":
            levelNum = 0

    elif num == 0.1:
        if sel == "help":
            helpRooms(["walk", "enter restart door"])

        elif sel == "walk":
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
    
    # Entrences:
    # Level 4.3, rotten wooden door
    # The Hub, moldy door
    elif num == 0.11:
        good = 0

        if sel == "help":
            helpRooms(["walk back", "open wooden door", "open office door", "enter flooded hole", "walk and open door"])

        elif sel == "walk back":
            levelNum = 0
        
        ranInt = random.randint(1, 7)
        if ranInt <= 4:
            good = 1
        elif ranInt > 5:
            death("an entity")
        
        if good == 1:
            if sel == "open wooden door":
                levelNum = 0
            elif sel == "open office door":
                levelNum = 4
            elif sel == "enter flooded hole":
                ranInt = random.randint(1, 2)
                if ranInt == 1:
                    levelNum = 8
                else:
                    levelNum = 7
            elif sel == "walk and open door":
                ranInt = random.randint(1, 5)
                if ranInt == 5:
                    levelNum = 0.7
                else:
                    msg = "You walk, but find no door"
        
    elif num == 0.2:
        if sel == "help":
            helpRooms(["open door with round handle", "noclip"])
            
        good = 0
        ranInt = random.randint(1, 20)
        if ranInt <= 12:
            good = 1
        elif ranInt > 12:
            death("turning into an Insanity")
        
        if good == 1:
            if sel == "open door with round handle":
                ranInt = random.randint(1, 5)
                ranInt2 = random.randint(1, 20)
                if ranInt2 == 20:
                    levelNum = 1
                elif ranInt == 1:
                    levelNum = 0
                elif ranInt == 2:
                    levelNum = "0.0"
                elif ranInt == 3:
                    levelNum = 0.1
                elif ranInt == 4:
                    levelNum = 0.3
                elif ranInt == 5:
                    levelNum = 0.4
            elif sel == "noclip":
                ranInt = random.randint(1, 7)
                if ranInt == 7:
                    levelNum = -132

    elif num == 0.22:
        if sel == "help":
            helpRooms(["walk", "enter vent"])

        good = 0
        ranEnt = random.randint(1, 10)
        if ranEnt == 10:
            death()
        else:
            good = 1
        
        if good == 1:
            if sel == "walk":
                ranInt = random.randint(1, 10)
                if ranInt > 6:
                    levelNum = 0
            elif sel == "enter vent":
                levelNum = 3

    elif num == 0.3:
        if sel == "help":
            helpRooms(["open emergency door"])

        good = 0
        ranEnt = random.randint(1, 10)
        if ranEnt >= 7:
            death()
        else:
            good = 1

        if good == 1:
            if sel == "open emergency door":
                if random.randint(1, 2) == 1:
                    levelNum = -1
                else:
                    levelNum = -2
            elif sel == "open employees only door":
                levelNum = 0.3

    # Entrences
    # 3.1, broken trapdoor
    # 0.9, noclip piping
    # use catatonia
    elif num == 0.4:
        if sel == "help":
            helpRooms(["break and enter window", "noclip in mold", "dig through floor with gear", "electrocute yourself", "open green door"])

        good = 0
        ranEnt = random.randint(1, 10)
        if ranEnt >= 7:
            death()
        else:
            good = 1

        if good == 1:
            if sel == "break and enter window":
                levelNum = 1.5
            elif sel == "noclip in mold":
                levelNum = 2
            elif sel == "dig through floor with gear":
                levelNum = "The End"
            elif sel == "electrocute yourself":
                levelNum = 3
            elif sel == "open green door":
                levelNum = 18
    
    elif num == 0.45:
        if sel == "help":
            helpRooms(["walk"])
        
        good = 0
        ranEnt = random.randint(1, 10)
        if ranEnt > 8:
            death()
        else:
            good = 1
        
        if good == 1:
            if sel == "walk":
                ranInt = random.randInt(1, 25)
                if ranInt == 25:
                    playerItems.append("a white door")
                    msg = "You found a white door!"
                elif ranInt == 24:
                    levelNum = 0
                    msg = "You found a key and teleported here!"
            elif sel == "open white door" and playerItems.count("a white door") > 0:
                levelNum = 0
        try:
            playerItems.remove("a white door")
        except:
            return

    else:
        win()

while True:
    clear()
    level(levelNum)