balance = float(input("Enter opening balance: "))
limit = float(input("Enter maximum withdrawal limit: "))

deposits = 0
withdrawals = 0
rejected = 0

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit  2. Withdraw")
    choice = int(input("Enter choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
        rejected += 1

    elif choice == 1:
        balance += amount
        deposits += 1
        print("Deposit successful")

    elif choice == 2:
        if amount > limit:
            print("Withdrawal limit exceeded")
            rejected += 1
        elif amount > balance:
            print("Insufficient balance")
            rejected += 1
        else:
            balance -= amount
            withdrawals += 1
            print("Withdrawal successful")

    else:
        print("Invalid transaction type")
        rejected += 1

print("\n--- Transaction Summary ---")
print("Final Balance:", round(balance, 2))
print("Successful Deposits:", deposits)
print("Successful Withdrawals:", withdrawals)
print("Rejected Transactions:", rejected)
