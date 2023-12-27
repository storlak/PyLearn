l = ['AAPL', 'AAPL', 'Aapl', 'aapl', 'MSFT']
unique_list  = set(l)
print(unique_list)

l2 = []
for symbol in l:
    l2.append(symbol.casefold())
unique_list = set(l2)
print(unique_list)