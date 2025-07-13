#writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    
#reading from a file
with open("sample.txt", "r") as file:
    data=file.read()
    print(data)