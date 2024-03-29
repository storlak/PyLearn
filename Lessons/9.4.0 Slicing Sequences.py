s = "Python rocks!"
print(s[5])
print(s[0:5])

t = [1, 2, 3, 4, 5]
print(t[1:4])
t2 = t[:]  # this is shallow copy
print(t2)
print(t is t2)  # shallow copy is different. not same nor identical

zoo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(zoo[1:8:2])
print(zoo[0::2])
print(zoo[1::2])
print(zoo[-3:])
zoo.reverse()  # reversing the list
print(zoo)
