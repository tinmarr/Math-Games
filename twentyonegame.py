import time, random

def Start():
    print("Welcome to the 21 Math Game!!\nThe rules are simple:\nTake away 1,2, or 3 bars at a time to end up taking the last bar.")
    while True:
        gamemode = input("What gamemode would you like to play? [Easy, Normal, Hard]")
        gamemode = gamemode.lower()
        if gamemode in ["easy", "normal", "hard"]:
            if gamemode == "easy":
                Easy()
            if gamemode == "normal":
                Normal()
            if gamemode == "hard":
                Hard()
        if input("Would you like to play again? [y/n]").lower() in ["y","yes"]:
            pass
        else:
            break


def PrintOrganized(n):
    n = int(n)
    n1 = n%4
    divisible = n - n1 
    numofrows = divisible/4
    numofrows = int(numofrows)
    for i in range(numofrows):
        print("|   "*4)
    if n1 == 1:
        print(f'{" "*6}|{" "*6}')
    if n1 == 2:
        print(f'{" "*4}|{" "*3}|')
    if n1 == 3:
        print(f'{" "*2}|{" "*3}|{" "*3}|')

def PrintUnOrganized(n):
    n = int(n)
    r = random.randint(1,n)
    ri = []
    for i in range(r):
        r1 = random.randint(1,n)
        ri.append(r1)
    ns = 0
    for i in range(n):
        if i in ri:
            print(" ", end="  ")
            ns += 1
        else:
            print("|",end="  ")
        if random.randint(1,5) == 1:
            print("")
    for i in range(ns):
        print("|", end="  ")
        if random.randint(1,5) == 1:
            print("")
    print("")


def Easy():  #Organized graph
    n = 21
    PrintOrganized(n)
    while True:
        remove = input("How many would you like to remove. [1,2,3]")
        remove = int(remove)
        if remove in [1,2,3]:
            n = n - remove
            if n <= 0:
                winner = "The human"
                break
            print("The computer is deciding what to remove...")
            time.sleep(0.5)
            n1 = n%4
            if n1 == 0:
                r = random.randint(1,3)
                print(f"The computer removes {r}")
                n = n - r
            else:
                n = n - n1
                print(f"The computer removes {n1}")
            if n <= 0:
                winner = "The computer"
                break
            PrintOrganized(n)
        else:
            print("Not a valid number!")
    print(f'{winner} wins!')
        

def Normal():  #Not organized graph
    n = 21
    PrintOrganized(n)
    r = random.randint(1,3)
    print(f"The computer removes {r}")
    n = n - r
    PrintUnOrganized(n)
    while True:
        remove = input("How many would you like to remove. [1,2,3]")
        remove = int(remove)
        if remove in [1,2,3]:
            n = n - remove
            if n <= 0:
                winner = "The human"
                break
            print("The computer is deciding what to remove...")
            time.sleep(0.2)
            n1 = n%4
            if n1 == 0:
                r = random.randint(1,3)
                print(f"The computer removes {r}")
                n = n - r
            else:
                n = n - n1
                print(f"The computer removes {n1}")
            if n <= 0:
                winner = "The computer"
                break
            PrintUnOrganized(n)
        else:
            print("Not a valid number!")
    print(f'{winner} wins!')


def Hard():  
    n = 21
    PrintUnOrganized(n)
    while True:
        print("The computer is deciding what to remove...")
        time.sleep(0.2)
        n1 = n%4
        if n1 == 0:
            r = random.randint(1,3)
            n = n - r
            print(f"The computer removes {r}")
        else:
            n = n - n1
            print(f"The computer removes {n1}")
        if n <= 0:
            winner = "The computer"
            break
        remove = input("How many would you like to remove. [1,2,3]")
        remove = int(remove)
        if remove in [1,2,3]:
            n = n - remove
            if n <= 0:
                winner = "The human"
                break
            PrintUnOrganized(n)
        else:
            print("Not a valid number!")
    print(f'{winner} wins!')
