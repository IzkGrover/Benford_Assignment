import matplotlib
import os

folder = os.getcwd()

def printMenu():
    print('''
          Customer and Sales System\n
          1. Load Sales File\n
          2. Analyze File\n
          3. Generate Graph\n
          9. Quit\n
          Enter menu option (1-9)
          ''')

def loadFile():
    fileName = folder + "\\sales.csv"
    file = open(fileName, "r")
    fileLines = file.readlines()

    return fileLines

def analyzeFile(file):
    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0
    number5 = 0
    number6 = 0
    number7 = 0
    number8 = 0
    number9 = 0

    for line in file:
        if "1" in line[4]:
            number1 = number1 + 1
        if "2" in line[4]:
            number2 = number2 + 1
        if "3" in line[4]:
            number3 = number3 + 1
        if "4" in line[4]:
            number4 = number4 + 1
        if "5" in line[4]:
            number5 = number5 + 1
        if "6" in line[4]:
            number6 = number6 + 1
        if "7" in line[4]:
            number7 = number7 + 1
        if "8" in line[4]:
            number8 = number8 + 1
        if "9" in line[4]:
            number9 = number9 + 1

    percent1 = number1/1620*100
    percent2 = number2/1620*100
    percent3 = number3/1620*100
    percent4 = number4/1620*100
    percent5 = number5/1620*100
    percent6 = number6/1620*100
    percent7 = number7/1620*100
    percent8 = number8/1620*100
    percent9 = number9/1620*100

    percentages = [percent1, percent2, percent3, percent4, percent5, percent6, percent7, percent8, percent9]

    return percentages


















































def generateGraph():
    pass


























userInput = ""
fileLoad = "1"
fileAnalyze = "2"
graphGeneration = "3"
exitCondition = "9"

while userInput != exitCondition:
    printMenu()                 
    userInput = input(); 

    if userInput == fileLoad:
        file = loadFile()

    elif userInput == fileAnalyze: 
        percentages = analyzeFile(file)
        print(percentages)
        

    elif userInput == graphGeneration: 
        generateGraph()

    else:
        print("Please type in a valid option (A number from 1-9)")

print("Program Terminated")