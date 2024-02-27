# Using a context manager for text files
with open("vbfiyat.txt") as f:
    print(f.closed)
print(f.closed)

with open("vbfiyat.txt", encoding="utf-8") as f:
    for line in f:
        print(line)
