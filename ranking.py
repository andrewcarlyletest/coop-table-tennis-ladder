#Used to determine how much a single game will change each player's rating
RANKING_CONSTANT = 50

#Return a list of all the players in the system
def getPlayerList():
    f = open("rankings.txt", "r")

    playerList = []
    counter = 1

    for player in f.readlines():
        player = player.strip().split(",")
        playerList.append({"number":counter, "name":player[0], "email":player[1], "rating":player[2]})
        counter += 1

    f.close()

    return playerList

#Get input from the user on which players were playing, and who won
def getMatchData():
    playerList = getPlayerList()
    print("\nHere is a list of all players in the system:")

    for player in playerList:
        print(str(player["number"]) + ") " + player["name"])

    winner = input("\nPlease select the number of the winning player: ")
    loser = input("Please select the number of the losing player: ")

    calculateRankings(playerList[int(winner)-1], playerList[int(loser)-1])

#Calculate the new rating points of each player based on the Elo rating system
def calculateRankings(p1, p2):
    r1 = float(p1["rating"])
    r2 = float(p2["rating"])

    print("\n" + p1["name"] + " rating before match: " + p1["rating"])
    print(p2["name"] + " rating before match: " + p2["rating"])

    e1=10**(r1/400)
    e2=10**(r2/400)

    n1=r1+RANKING_CONSTANT*(1-(e1/(e1+e2)))
    n2=r2+RANKING_CONSTANT*(0-(e2/(e1+e2)))

    print("\n" + p1["name"] + " new rating: " + str(n1))
    print(p2["name"] + " new rating: " + str(n2))

    f = open("rankings.txt", "r")
    players = f.readlines()
    f.close()

    players[p1["number"]-1] = p1["name"] + "," + p1["email"] + "," + str(n1) + "\n"
    players[p2["number"]-1] = p2["name"] + "," + p2["email"] + "," + str(n2) + "\n"

    f = open("rankings.txt", "w")
    f.writelines(players)
    f.close()

#Adds a new player with an inital rating of 1000
def addPlayer():
    name = input("Please enter your first and last name: ")
    email = input("Please your Nokia email: ")

    f = open("rankings.txt", "a")

    f.write("\n" + name + "," + email + ",1000")
    f.close()

    print("Thanks " + name + ", you've been added to the list with a starting rating of 1000!")

selection = input("Welcome, please enter one of the following numbers: \n1) Add a new player to the system \n2) Enter the result of the game \n3) Show the leaderboard\n")

if selection == "1":
    addPlayer()
elif selection == "2":
    getMatchData()
else:
    playerList = getPlayerList()
    print(playerList)
