f = open("demofile.txt", "w")
f.write("Opps! I have deleted the content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
