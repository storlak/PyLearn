s1 = set("abc")
s2 = {True, False}
s3 = {"a", 100, 300}

print(s1.isdisjoint(s3)) # will print False
print(s1 | s3 | s2) # union of sets
print(s1 & s3)  # intersection
print(s1 - s3)
