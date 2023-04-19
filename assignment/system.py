from matplotlib import pyplot as plt

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
    file = open("sales.csv", "r")
    fileLines = file.readlines()
    file.close()

    print("File Loaded")
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
    length = 0

    for line in file:
        if "1" in line[4]:
            number1 = number1 + 1
            length = length + 1
        if "2" in line[4]:
            number2 = number2 + 1
            length = length + 1
        if "3" in line[4]:
            number3 = number3 + 1
            length = length + 1
        if "4" in line[4]:
            number4 = number4 + 1
            length = length + 1
        if "5" in line[4]:
            number5 = number5 + 1
            length = length + 1
        if "6" in line[4]:
            number6 = number6 + 1
            length = length + 1
        if "7" in line[4]:
            number7 = number7 + 1
            length = length + 1
        if "8" in line[4]:
            number8 = number8 + 1
            length = length + 1
        if "9" in line[4]:
            number9 = number9 + 1
            length = length + 1

    percent1 = round(number1/length*100, 2)
    percent2 = round(number2/length*100, 2)
    percent3 = round(number3/length*100, 2)
    percent4 = round(number4/length*100, 2)
    percent5 = round(number5/length*100, 2)
    percent6 = round(number6/length*100, 2)
    percent7 = round(number7/length*100, 2)
    percent8 = round(number8/length*100, 2)
    percent9 = round(number9/length*100, 2)

    percentages = [percent1, percent2, percent3, percent4, percent5, percent6, percent7, percent8, percent9]

    if 29 <= percent1 <= 32:
        print("1:", percent1, "2:", percent2, "3:", percent3, "4:", percent4, "5:", percent5, "6:", percent6, "7:", percent7, "8:", percent8, "9:", percent9)
        print("Based on your data fraud likely did not occur")
    else:
        print("1:", percent1, "2:", percent2, "3:", percent3, "4:", percent4, "5:", percent5, "6:", percent6, "7:", percent7, "8:", percent8, "9:", percent9)        
        print("Based on your data fraud likely did occur")

    return percentages

def generateGraph(percentages):

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
    plt.close()

    table = "1" + "," + "2" + "," + "3" + "," + "4" + "," + "5", "," + "6" + "," + "7" + "," + "8" + "," + "9\n" + str(percentages[0]) + "," + str(percentages[1]) + "," + str(percentages[2]) + "," + str(percentages[3]) + "," + str(percentages[4]) + "," + str(percentages[5]) + "," + str(percentages[6]) + "," + str(percentages[7]) + "," + str(percentages[8])
    result_fileName = "results.csv"
    result_file = open(result_fileName, "w")
    result_file.writelines(table)
    result_file.close()

userInput = ""
fileLoad = "1"
fileAnalyze = "2"
graphGeneration = "3"
exitCondition = "9"

while userInput != exitCondition:
    printMenu()                
    userInput = input()

    if userInput == fileLoad:
        file = loadFile()

    elif userInput == fileAnalyze:
        percentages = analyzeFile(file)

    elif userInput == graphGeneration:
        generateGraph(percentages)

    else:
        print("Please type in a valid option (A number from 1-9)")

print("Program Terminated")

