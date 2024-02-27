my_file = open("vbfiyat.txt", "r")
print(my_file.name)
print(my_file.readable())  # True if file is readable
print(my_file.writable())  # True if file is readable
print(my_file.closed)  # false if open
my_file.close()  # closes the open file.
print(my_file.closed)  # false if open
