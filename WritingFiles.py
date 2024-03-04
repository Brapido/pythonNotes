# writing to a file using "a" for append
# writing to a file using "w" will overwrite entire file
def example():
    with open("users.txt", "a") as file:
        print("Please enter a new name: ")
        name = str(input())
        file.write("\n" + name)

    # read the file
    with open("users.txt.", "r") as file:
        for line in file:
            print(line)
