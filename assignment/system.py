import matplotlib.pyplot as plt
import os

folder = os.getcwd()

def printMenu():
    '''
    Displays a menu for the user. Lists the numbers the user needs to input to access
    the functions of the sales system.
    '''
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
    '''
    Analyzes the csv file to check which sales data in the file is valid or fraud. It does this
    by using benford's law which finds the frequency of the first digit and then checks if it is 
    between 29% and 32%. If it is, the data is valid, if it isn't, the data is fraud. 
    
    Parameters:
                file: The csv sales data file that was read and returned
    '''




def generateGraph(percentages):
    '''
    This function uses the information given by the analyzation function to create a bar graph based
    on the sales data. The graph is then put into a new file along with the sales data in a file. 
    
    Parameters:
                percentages: The frequency of the first digits analyzed in the sales data 
    '''
    x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y_values = percentages
    y_value1 = "1 = " + str(y_values[0]) + "%"
    y_value2 = "2 = " + str(y_values[1]) + "%"
    y_value3 = "3 = " + str(y_values[2]) + "%"
    y_value4 = "4 = " + str(y_values[3]) + "%"
    y_value5 = "5 = " + str(y_values[4]) + "%"
    y_value6 = "6 = " + str(y_values[5]) + "%"
    y_value7 = "7 = " + str(y_values[6]) + "%"
    y_value8 = "8 = " + str(y_values[7]) + "%"
    y_value9 = "9 = " + str(y_values[8]) + "%"

    plt.bar(x_values[0], y_values[0], color="red")
    plt.bar(x_values[1], y_values[1], color="green")
    plt.bar(x_values[2], y_values[2], color="blue")
    plt.bar(x_values[3], y_values[3], color="orange")
    plt.bar(x_values[4], y_values[4], color="yellow")
    plt.bar(x_values[5], y_values[5], color="pink")
    plt.bar(x_values[6], y_values[6], color="purple")
    plt.bar(x_values[7], y_values[7], color="black")
    plt.bar(x_values[8], y_values[8], color="brown")

    plt.title("Benford's Law Distribution Leading Digit")
    plt.legend([y_value1, y_value2, y_value3, y_value4, y_value5, y_value6, y_value7, y_value8, y_value9], loc=0)
    plt.xlabel("Digit")
    plt.ylabel("Percent")
    plt.show()
    image = plt.savefig("graph.png")
    plt.close()

    location = 0 
    plt.legend(["blue", "red"], loc=0)

    plt.xlabel("Digit")
    plt.ylabel("Percent")

    plt.show()
    
    picture = plt.savefig("ResultsGraph.png", bbox_inches="tight")
    
    plt.close(plt)
    
    result_fileName = folder + "\\" + "results.csv"
    result_file = open("results.csv", "w")
    result_file.write(percentages)
    result_file.write(picture)
    result_file.close()
    picture_fileName = folder + "\\" + "ResultsGraph.png"
    result_file_pic = open("ResultsGraph.png", "w")
    result_file_pic.write(picture)
    result_file_pic.close()
    



























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
        generateGraph(percentages)

    else:
        print("Please type in a valid option (A number from 1-9)")

print("Program Terminated")
