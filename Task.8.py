with open("output.txt", "r") as file:
    Data = file.read()

with open("output.txt", "w") as file:
    Data = file.write("Hello,Python!")

with open("output.txt", "r") as file:
    Data = file.read()
    print(Data)

with open("output.txt", "a") as file:
    Data = file.write(" \nLearning file handling in python")
    print(Data)

with open("output.txt", "r") as file:
    Data = file.read()
    print(Data)