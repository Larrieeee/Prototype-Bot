# Variables --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Yoo prefix for our bot
yooLowerList = []
yooUpperList = []

# Functions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def capYoooo(repeatAmount):
    yooUpper = "YO"

    for i in range(0, repeatAmount):
        yooUpper += "O"
        yooUpperList.append(yooUpper)
        
        # Remember that this is an empty list 
        yooUpperList[i] += " "

    return yooUpperList


def lowYoooo(repeatAmount):
    yooLower = "yo"

    for i in range(0, repeatAmount):
        yooLower += "o"
        yooLowerList.append(yooLower)
        
        # Remember that this is an empty list 
        yooLowerList[i] += " "
    
    return yooLowerList

def yooPrefix():
    return capYoooo(100) + lowYoooo(100)

# MainSetup --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
