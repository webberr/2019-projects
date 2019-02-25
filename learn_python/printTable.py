#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)

def printTable():
    for i in range(len(tableData[0])):
        print(tableData[0][i].rjust(8) + " " +tableData[1][i].rjust(8) + " " + tableData[2][i].rjust(8))

printTable()