class Player:

    playerName = None
    playerPos = None
    playerAvgPoints = None
    playerSalary = None

    def __init__(self, playerName, playerPos, playerAvgPoints, playerSalary):

        self.playerName = playerName
        self.playerPos = playerPos
        self.playerAvgPoints = playerAvgPoints
        self.playerSalary = playerSalary

    """"
    Below are the setters
    """
    def setPlayerName(self, playerName):
        self.playerName = playerName

    def setPlayerPos(self, playerPos):
        self.playerPos = playerPos

    def setPlayerAvgPoints(self, playerAvgPoints):
        self.playerAvgPoints = playerAvgPoints

    def setPlayerSalary(self, playerSalary):
        self.playerSalary = playerSalary

    """"
    below are the getters
    """
    def getPlayerName(self):
        return self.playerName

    def getPlayerPos(self):
        return self.playerPos

    def getPlayerAvgPoints(self):
        return self.playerAvgPoints

    def getPlayerSalary(self):
        return self.playerSalary

    #prints out the players information
    def displayPlayer(self):
        print("Player Name: ", self.playerName)
        print("Player Position: ", self.playerPos)
        print("Player Salary: $", self.playerSalary)
        print("Player Avg. Points: ", self.playerAvgPoints)
