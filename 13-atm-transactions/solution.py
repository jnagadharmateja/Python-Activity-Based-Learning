balance = 1000.0
deposits = 0.0
withdrawals = 0.0
rejected = 0
count = int(input("Number of transactions: "))
if count < 0:
    print("Invalid transaction count.")
else:
    for i in range(count):
        kind = input("Type (D/W): ").strip().upper()
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Rejected: amount must be positive")
            rejected += 1
        elif kind == "D":
            balance += amount
            deposits += amount
            print("Deposit accepted")
        elif kind == "W" and amount <= 5000 and amount <= balance:
            balance -= amount
            withdrawals += amount
            print("Withdrawal accepted")
        else:
            print("Rejected: type, limit or balance")
            rejected += 1
    print("Deposits: Rs", format(deposits, ".2f"))
    print("Withdrawals: Rs", format(withdrawals, ".2f"))
    print("Rejected:", rejected)
    print("Balance: Rs", format(balance, ".2f"))
