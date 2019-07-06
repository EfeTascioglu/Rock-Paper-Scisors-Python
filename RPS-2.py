import random

playerWin = [1,-2]
validChoices = [ "0","1","2" ]
choices = ["rock", "paper", "scissors"]
whoPlayed = [ "Computer chose", "Player chose" ]
computerChoice = 0
playerChoice = 0

keepGoing = True
P1 = 0  #Points for P1
C = 0   #Points for Com
def getValidData(validChoices):
    validData = input("Enter 0 for rock, 1 for paper, 2 for scissors")
    notValidData = not (validData in validChoices)
    while notValidData:
        print("You have made an error")
        validData = input("Enter 0 for rock, 1 for paper, 2 for scissors")
        notValidData = not (validData in validChoices)
    validData = int(validData)
    return validData
print(getValidData)

def getBothPlayers(validChoices):
    keepGoing = True
    while keepGoing:
        comValue = random.randint(0,2)
        P1Value = int( getValidData(validChoices) )
        keepGoing = (comValue == P1Value)
        print("The computer played a " + choices[comValue] + "!")
        if keepGoing:
            print("It was a draw,")
    return (comValue, P1Value)

def Winner(P1,C):
    (comValue,P1Value) = getBothPlayers(validChoices)
    if ((P1Value-comValue) in playerWin):
        P1 += 1
        print("Your",choices[P1Value], "has defeated the computers",choices[comValue] + "!")
        print("The scores are now:", P1,":",C)
    else:
        C += 1
        print("Your", choices[P1Value], "was defeated  by the computers", choices[comValue] + "!")
        print("The scores are now:", P1, ":", C)
    return(P1,C)


while keepGoing:
    P1,C = Winner(P1,C)
    keepGoing = (P1 < 3) and (C < 3)