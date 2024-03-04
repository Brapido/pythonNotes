# open file for reading "r"
# with block automatically closes() file
def example():
    with open("users.txt", "r") as file:
        for line in file:
            print(line)

    # returns boolean if file has been closed
    print(file.closed)
