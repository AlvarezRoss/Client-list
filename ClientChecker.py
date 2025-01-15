import csv
import sys
import random
import pandas as pad
def main():
    Clients = []
    LenthArgv = len(sys.argv)
    ClientFound = False
    if LenthArgv != 2:
        print("Error - usage - name of program and client Name")
        sys.exit(1)
    with open("clients.csv") as csv_file:
        Reader = csv.DictReader(csv_file)
        for row in Reader:
            Clients.append(row)
        for name in Clients:
            if sys.argv[1] == str(name["client"]):
                print(f"{sys.argv[1]} has been here before")
                ans = input("Do you want to register another client with the same name? ").lower
                if ans == "yes":
                    break
                else:
                    UpadteClient("clients.csv",name["Times"])
                    ClientFound = True
                    break
        if not ClientFound:
            print(f"{sys.argv[1]} has not been here before")
            NewClient("clients.csv")
    
def NewClient(file):
    with open(file, "a", newline="") as csv_clients:
        writer = csv.writer(csv_clients)
        ID = random.randrange(1,1000)
        ClientName = input("What is the client's name? ")
        if not any(char.isdigit() for char in ClientName):
            NewClient = (ClientName, ID, 0)
            writer.writerow(NewClient)
        else:
            print("invalid name")
            sys.exit(1)
        return
def UpadteClient(file,Times):
    Updater = pad.read_csv(file,index_col = 0)
    Times = int(Times)
    Updater.loc[sys.argv[1], "Times"] = Times + 1
    Updater.to_csv(file)
main()