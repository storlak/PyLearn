for i in range(1, 5):
    for j in range(1, 5):
        if (i + j) % 2 == 1:
            print(f"{i} + {j} is odd, skipping...")
            continue # continue here applies to the "j" loop not i loop!!!
        print(f"adding numbers {i} + {j} = {i + j}")
    print("-" * 10)

for i in range(1, 4):
    for j in range(1, 4):
        if j >=3:
            break
        print((i, j))
    print("-" * 5)
