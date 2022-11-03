
from contextlib import nullcontext
import csv
from tabulate import tabulate

def readrawfile():
    with open('Data.csv', newline='') as f:
        reader = csv.reader(f)
        return list(reader)

def processdata(rawdata):
    classcodeEng = ["14B1", "15B1", "14B2", "15B2", "14B3", "15B3", "1411", "1511", "1412", "1512", "1413", "1513", "1514 IELTS", "1515 IELTS", "1516 IELTS"]
    for row in rawdata:
        for element in row:
            splitemlement = element.encode('cp1252').decode('utf8').split(";")
            print(splitemlement)
            # if splitemlement[0] in classcodeEng:
            #     print(splitemlement)

            #     # Next Element
            #     nextElement = row[row.index(element)+1]
            #     splitNextEmlement = nextElement.encode('cp1252').decode('utf8').split(";")
            #     print(splitNextEmlement)
            #     print("\n")

            


def drawtable():    
    #create data
    data = [["Shift 1", "", "", "", "", "", "", ""], 
            ["Shift 2", "", "", "", "", "", "", ""], 
            ["Shift 3", "", "", "", "", "", "", ""], 
            ["Shift 4", "", "", "", "", "", "", ""]]
    
    #define header names
    col_names = ["", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    #display table
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))



def main():
   readrawfile()
   processdata(readrawfile())
#    drawtable()

if __name__ == "__main__":
    main()

