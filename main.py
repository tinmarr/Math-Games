import twentyonegame

while True:
    print("Welcome to Math Games!\nInstructions for each game are in the game start text.\nType 'exit' to exit the game.")
    game = input("What game would you like to play? [21]")
    print("\n")
    game = game.lower()
    if game == "exit":
        break
    elif game in ["21"]:
        if game == "21":
            twentyonegame.Start()