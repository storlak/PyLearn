# Case Mapping
print("Hello World".lower())
print("Hello World".upper())
print("one, two, three".title())

s1 = "hello"
s2 = "HeLlo"
print(s1.casefold() == s2.casefold())

# stripping
# .lstrip() or .rstrip() or .strip() or .strip(" "), .strip("a","b","c")
name = "ababPythonabab"
print(name.strip("ab")) 

# concatenating
print("Hello" + " " + "World")

# splitting
data = "100, 200, 300, 400"
print(data.split(","))  # returns a list of splitted elements.

# joining
print(",".join(["10", "20", "30"]))
data = ("ab", "cd", "ef")
print("--".join(data))

# finding substrings
# we use in or index or find
# x in xyz -----> TRUE
# a in xyz -----> FALSE

# .startswith("...") or .endswith("...")
