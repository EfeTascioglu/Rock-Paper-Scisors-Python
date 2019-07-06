import random

playerWin = [1,-2]
validChoices = [ "0","1","2" ]
choices = ["rock", "paper", "scissors"]
whoPlayed = [ "Computer chose", "Player chose" ]
computerChoice = 0
playerChoice = 0
mode = 0

keepGoing = True
P1 = 0  #Points for P1
C = 0   #Points for Com
def getValidData(validChoices,mode):
    validData = input("Enter 0 for rock, 1 for paper, 2 for scissors")
    notValidData = not (validData in validChoices)
    if validData == "l":
        mode = 1
    if validData == "w":
        mode = 2
    while notValidData:
        print("You have made an error")
        validData = input("Enter 0 for rock, 1 for paper, 2 for scissors")
        notValidData = not (validData in validChoices)
    validData = int(validData)
    return validData , mode

def getBothPlayers(validChoices,mode):
    keepGoing = True
    while keepGoing:
        comValue = random.randint(0,2)
        P1Value , mode = getValidData(validChoices,mode)
        if mode == 1:
            if (P1Value == 0) or (P1Value == 1):
                comValue = P1Value + 1
            else:
                comValue = 0
        if mode == 2:
            if (P1Value == 1) or (P1Value == 2):
                comValue = P1Value - 1
            else:
                comValue = 2
        keepGoing = (comValue == P1Value)
        print("The computer played a " + choices[comValue] + "!")
        if keepGoing:
            print("It was a draw,")
    return (comValue, P1Value, mode)

def Winner(P1,C,mode):
    (comValue,P1Value,mode) = getBothPlayers(validChoices,mode)
    if ((P1Value-comValue) in playerWin):
        P1 += 1
        print("Your",choices[P1Value], "has defeated the computers",choices[comValue] + "!")
        print("The scores are now:", P1,":",C)
    else:
        C += 1
        print("Your", choices[P1Value], "was defeated  by the computers", choices[comValue] + "!")
        print("The scores are now:", P1, ":", C)
    return(P1,C,mode)


while keepGoing:
    P1,C,mode = Winner(P1,C,mode)
    keepGoing = (P1 < 3) and (C < 3)