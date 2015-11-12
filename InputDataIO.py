import win32api, win32con
import actionFunctions

#Write Function for AI
#Text format:
# [goodness number] [distance from ground] [distance from pipe]
#returns a list of the last iteration's input values


def writeToFile(goodness, distFromGround, distFromPipe)
    outputFile = open("BotInputData.txt", 'w')
    if (outputFile):
        outputFile.write(str(goodness))
        outputFile.write(' ')
        outputFile.write(str(distFromGround))
        outputFile.write(' ')
        outputFIle.write(str(distFromPipe))
        outputFile.write('\n')
    outputFile.close()


def readFromFile()
    inputFile = open("BotInputData.txt")
    for line in inputFile:
        inputData = line.split()
        return inputData


    
        
