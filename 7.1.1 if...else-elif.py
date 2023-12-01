account_enabled = True
balance = 1000
withdraw = 100_000

if not account_enabled:
    print("Your account is disabled.")
elif withdraw > balance:
    print("Insufficient funds.")
else:
    print("Withdrawal authorized!")
