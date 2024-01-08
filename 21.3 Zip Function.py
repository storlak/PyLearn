# zip function returns and iterator that produces tuples
l1 = ["a", "b", "c", "d", "e"]
l2 = [34, 35, 48]
l3 = ["Istanbul", "İzmir", "Muğla"]
combo = list(zip(l1, l2))
print(combo)

# zip is extensible
combowombo = zip(l1, l2, l3)
