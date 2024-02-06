f = open("demofile3.csv", "w")
f.write("abc")
f.write("123456")
f.close()

with open("demofile3.csv", "r") as f:
    print(f.readlines())

with open("demofile3.csv", "w") as f:
    f.write("abc\n")
    f.write("123456\n")

with open("demofile3.csv", "r") as f:
    print(f.readlines())

data = ["line 1\n", "line 2\n", "line 3\n"]
with open("demofile3.csv", "w") as f:
    f.writelines(data)
with open("demofile3.csv", "r") as f:
    print(f.readlines())
with open("demofile3.csv", "r") as f:
    for line in f:
        print(line, end="")
with open("demofile3.csv", "a") as f:
    f.write("line 4\n")
    f.write("line 5\n")
with open("demofile3.csv") as f:
    print()
    for line in f:
        print(line.strip())
