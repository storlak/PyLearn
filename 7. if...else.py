account_enabled = True
balance = 1000
withdraw = 100_000

if account_enabled and withdraw <= balance:
    print("Withdrawal authorized.")
else:
    if not account_enabled:
        print("Withdrawal not authorized.")
    else:
        print("Insufficient funds.")
