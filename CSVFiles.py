import csv

"""""

"""""


class User:
    name: str
    email: str

    # Constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email


def menu():
    print("What would you like to do?")
    print("0: to exit")
    print("1: Read CSV")
    print("2: ")
    x = int(input())

    while x != 0:
        match x:
            case 1:
                readCSV()
                x = 0
            case 2:
                pass
            case default:
                print("invalid choice try again")


def readCSV():
    with open("users.csv") as file:
        reader = csv.reader(file, delimiter=",")
        '''
        # this prints each line in a matrix represented by csv file.
        for line in reader:
            print(line)
    
        '''
        user_list = []
        # row_number = 1 ignores first row of csv file in our for loop. not sure why but it does...
        row_number = 1
        for x in reader:
            if row_number != 1:
                user = User(x[0] + " " + x[1], x[2])
                user_list.append(user)
                row_number += 1
            else:
                row_number += 1


    print(user_list)
    print(user_list[0].name)

    for item in user_list:
        print(item.name + "!")
