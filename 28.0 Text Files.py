f = open("demofile.txt", "r")  # if no such file: returns an error.
print(f.read())
print(f.read(25))  # specify how many chars to return
print(f.readline())  # returns a line
f.close()  # closes the file.
