from Player import Player

#This method takes the name of a file and
#opens the file, and returns the header of the file
#and the contents of the file in list format.
def fileRead(fileName):

    theFile = open(fileName)

    theFile.readline() #this is just the header, the very first line
    fileList = theFile.readlines() #this is the whole list on one row

    return fileList


#creates a list of players, returns a list
#that has the players name, roster position,
#salary and average points
def createPlayerList(fileList):

    playerList = []

    for line in fileList:

        temp = line.split(",")
        player = Player(temp[2], temp[0], float(temp[8]), float(temp[5])) #manually looked at csv file to determine indices
        playerList.append(player) #populate list of players

    return playerList

#numofPlayersPerPosition gets the number of players per
#position returns it in a list format.
#[QB, RB, WR, TE, DST]
def numOfPlayersPerPositon(playerList):

    qbCounter = 0
    rbCounter = 0
    wrCounter = 0
    teCounter = 0
    dstCounter = 0

    numList = []

    for player in playerList:
        if(player.getPlayerPos() == 'QB' and player.getPlayerAvgPoints() > 0):
            qbCounter += 1

        if(player.getPlayerPos() == 'RB' and player.getPlayerAvgPoints() > 0):
            rbCounter += 1

        if(player.getPlayerPos() == 'WR' and player.getPlayerAvgPoints() > 0):
            wrCounter += 1

        if(player.getPlayerPos() == 'TE' and player.getPlayerAvgPoints() > 0):
            teCounter += 1

        if(player.getPlayerPos() == 'DST' and player.getPlayerAvgPoints() > 0):
            dstCounter += 1

    numList.append(qbCounter)
    numList.append(rbCounter)
    numList.append(wrCounter)
    numList.append(teCounter)
    numList.append(dstCounter)

    return numList

#getStarters gets the starters from the playerList, the
#playerList is the list with all of the players, each of the
#other lists are the starters at the given position
def getStarters(playerList, QB_list, RB_list, WR_list, TE_list):

    startersList = []
    #put an empty defense and special teams list here

    for player in playerList:

        if(player.getPlayerPos() == 'QB'): #checks QBs
            if(player.getPlayerName() in QB_list): #if QB is a starter
                startersList.append(player)

        elif(player.getPlayerPos() == 'RB'): #checks if RB is a starter
            if (player.getPlayerName() in RB_list):
                startersList.append(player)

        elif(player.getPlayerPos() == 'WR'): #checks if WR is a starter
            if (player.getPlayerName() in WR_list):
                startersList.append(player)

        elif(player.getPlayerPos() == 'TE'): #checks if TE is a starter
            if (player.getPlayerName() in TE_list):
                startersList.append(player)

        #create one more if statement for D/ST
        #append any D/ST to the defense list

    return startersList #return defense list too


#Breaks up the list of starters into seperate lists
#by position, groups the starters based off of their position
def positionBreakUp(starterList):

    QB_list = []
    RB_list = []
    WR_list = []
    TE_list = []

    for player in starterList:

        if(player.getPlayerPos() == 'QB'):
            QB_list.append(player)

        if(player.getPlayerPos() == 'RB'):
            RB_list.append(player)

        if(player.getPlayerPos() == 'WR'):
            WR_list.append(player)

        if(player.getPlayerPos() == 'TE'):
            TE_list.append(player)

    return QB_list, RB_list, WR_list, TE_list


#sorts the player list in descending order based
#off of the player's average points scored
#the player with the highest average points scored
#will be at the beginning of the list, and the player
#with the lowest average points scored will be at the
#end of the list. Bubble Sort was used.
def highestToLowestScore(playerList, emptyList): #need an empty list to save the 'playerList' value before sorting

    for player in playerList: #populate the empy list
        emptyList.append(player)

    for j in range(0, len(emptyList)): #make changes to 'emptyList' not 'playerList'

        checkForSwap = False

        for i in range(0, (len(emptyList) - 1)):

            if(emptyList[i].getPlayerAvgPoints() <= emptyList[i + 1].getPlayerAvgPoints()):

                lowerScore = emptyList[i]
                emptyList[i] = emptyList[i + 1]
                emptyList[i + 1] = lowerScore
                checkForSwap = True

                if(checkForSwap == False):
                    break

    return emptyList

#Does the same thing as highestToLowestScore, except
#instead of sorting it in decsending order by score
#it uses the player's salary. Bubble sort was used.
def highestToLowestSalary(playerList, emptyList): #empty list allows playerList to be saved

    for player in playerList: #populate the empty list
        emptyList.append(player)

    for j in range(0, len(emptyList)):

        checkForSwap = False

        for i in range(0, (len(emptyList) - 1)):

            if(emptyList[i].getPlayerSalary() <= emptyList[i + 1].getPlayerSalary()):

                lowerSalary = emptyList[i] #player with lower salary
                emptyList[i] = emptyList[i + 1] #swap players
                emptyList[i + 1] = lowerSalary #swap players
                checkForSwap = True

                if(checkForSwap == False):
                    break

    return emptyList

#puts together all the possible combinations with
#three players of a given position under $16,650
def combosOfThree(playerList):

    threeCombo = []
    for i in range(0, (len(playerList) - 2)): #0 -> third to last
        for j in range((i + 1), (len(playerList) - 1)): #i + 1 -> second to last
            for k in range((j + 1), len(playerList)): #j + 1 -> last

                #gets the total salary of  the three players added up
                totalPlayer_cap = playerList[i].getPlayerSalary() + \
                              playerList[j].getPlayerSalary() + \
                              playerList[k].getPlayerSalary()
                
                #salary can be edited here. I just have a number here 
                if(totalPlayer_cap <= 21000): #only combos under $20,000

                    tempPlayer_list = [playerList[i], playerList[j], playerList[k]] #create a temporary list
                    threeCombo.append(tempPlayer_list) #add temporary list to comboList

    return threeCombo

#gets the total score from  each combo from the comboList
#and returns a list with the index, and the inex's score.
def indicesAndScores(comboList, emptyList, returnList): #make edits later to refine it

    for combo in comboList:
        emptyList.append(combo)

    for i in range(0, len(emptyList)):

        totalScore = 0

        for j in range(0, len(emptyList[i])):

            totalScore += emptyList[i][j].getPlayerAvgPoints()

        returnList.append([i, totalScore])

    return returnList


def comboSort(scoreList):

    for i in range(0, len(scoreList)):
        for j in range(0, (len(scoreList) - 1)):

            if(scoreList[j][1] <= scoreList[j + 1][1]):

                lower = scoreList[j]
                scoreList[j] = scoreList[j + 1]
                scoreList[j + 1] = lower

    return scoreList



if __name__ == '__main__':

    a = fileRead("DKSalaries (1).csv")
    b = createPlayerList(a)

    QBs = fileRead("startingQBs.csv")
    RBs = fileRead("startingRBs.csv")
    TEs = fileRead("startingTEs.csv")
    WRs = fileRead("startingWRs.csv")

    #Create new lists to get rid of the '\n' for each string in the list
    new_RBs = [rb[:-1] for rb in RBs]
    new_QBs = [qb[:-1] for qb in QBs]
    new_WRs = [wr[:-1] for wr in WRs]
    new_TEs = [te[:-1] for te in TEs]

    c = getStarters(b, new_QBs, new_RBs, new_WRs, new_TEs)

    startingQBs, startingRBs, startingWRs, startingTEs = positionBreakUp(c) #get all starters
    flexList = startingRBs + startingWRs + startingTEs

    sortedByScoreRBs = highestToLowestScore(startingRBs, [])
    sortedBySalaryRBs = highestToLowestSalary(startingRBs, [])

    sortedByScoreQBs = highestToLowestScore(startingQBs, [])
    sortedBySalaryQBs = highestToLowestSalary(startingQBs, [])

    sortedByScoreWRs = highestToLowestScore(startingWRs, [])
    sortedBySalaryWRs = highestToLowestSalary(startingWRs, [])

    """"
    threeWRs = combosOfThree(sortedBySalaryWRs)
    indicesAndScoresWRs = indicesAndScores(threeWRs, [], [])
    sortedIndicesAndScores = comboSort(indicesAndScoresWRs)

    
    for i in range(0, 10):
        temp = threeWRs[sortedIndicesAndScores[i][0]]
        for j in range(0, len(temp)):
            print(temp[j].getPlayerName())
        
        print()
    print(sortedIndicesAndScores)
    """


    threeRBs = combosOfThree(sortedBySalaryRBs)

    indicesAndScores = indicesAndScores(threeRBs, [], [])
    sortedIndicesAndScores = comboSort(indicesAndScores)



    #prints the top 10 RB combos of three
    for i in range(0, 10):
        temp = threeRBs[sortedIndicesAndScores[i][0]]
        for j in range(0, len(temp)):
            print(temp[j].getPlayerName())

        print()
    
    print(sortedIndicesAndScores)

