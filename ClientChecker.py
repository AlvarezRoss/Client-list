import csv
import sys
import random
def main():
    Clients = []
    LenthArgv = len(sys.argv)
    if LenthArgv != 2:
        print("Error - usage - name of program and client name")
        sys.exit(1)
    with open("clients.csv") as csv_file:
        Reader = csv.DictReader(csv_file)
        for row in Reader:
            Clients.append(row)
        for name in Clients:
            if sys.argv[1] == name["client"]:
                print(f"{sys.argv[1]} was here")
                break
            else:
                print(f"{sys.argv[1]} was not here")
                NewClient("clients.csv")
                break
    
def NewClient(file):
    with open(file, "a", newline="") as csv_clients:
        writer = csv.writer(csv_clients)
        ID = random.randrange(1, 10000)
        NewClient = (sys.argv[1], ID, 0)
        writer.writerow(NewClient)
        return
main()