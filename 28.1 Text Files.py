f = open("demofile.txt", "a")
f.write("\nNow the file has more content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
