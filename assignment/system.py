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
    pass




def generateGraph():
    x_values = []
    y_values = []

    x_values_2 = []
    y_values_2 = []

    plt.bar(x_values_2, y_values_2, color="navy")
    plt.bar(x_values, y_values, color="red")

    plt.title("Benford's Law Distribution Leading Digit")

    location = 0 # For the best location
    plt.legend(["blue", "red"], loc=0)


    plt.xlabel("Digit")
    plt.ylabel("Percent")

    plt.show()

    result_fileName = folder + "\\" + "results.csv"
    result_file = open("results.csv", "w")
    result_file.write(percentages)
    result_file.close()
    



























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
