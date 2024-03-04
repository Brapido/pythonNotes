"""""
###NOTES###
writing to a file modifiers:
"r" will read file
"a" will append
"w" will overwrite entire file
"r+" read and write

with open("File Name", "modifier") as file:
    This will open close a file without the need to close it at the end.  close().
"""


def menu():
    print("What would you like to do?")
    print("0: to exit")
    print("1: Read and write")
    print("2: Add using file")
    x = int(input())

    while x != 0:
        match x:
            case 1:
                readwrite()
                x = 0
            case 2:
                total = adding()
                print("The running total for numbers file is: ", total)
                x = 0
            case default:
                print("invalid choice try again")



def readwrite():
    with open("users.txt", "a") as file:
        print("Please enter a new name: ")
        name = str(input())
        file.write("\n" + name)

    # read the file
    with open("users.txt.", "r") as file:
        for line in file:
            print(line)


def adding():
    x = 0
    with open("numbers.txt", "r") as file:
        for line in file:
            x = int(line) + x
    return x
