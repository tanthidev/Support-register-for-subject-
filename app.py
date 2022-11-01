
import csv

def readfile():
    with open('Data.csv') as f:
       reader = csv.reader(f)
       for row in reader:
            for a in row:
                print(a.encode('cp1252').decode('utf8'))
            print("\n")





def main():
   readfile()

if __name__ == "__main__":
    main()
