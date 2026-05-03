# Exercise 2: Simulates a bank account by tracking deposits and withdrawals, calculating the final balance and total number of withdrawals made.
initial_amount = 10000

transactions = [2000, -500, 3000, -1500, 4000, -2500, 3500, -1000]
count = 0
for amount in transactions:
    if amount <0:
        print(f"Withdrawal: ${abs(amount):,.2f}")
        count += 1
    elif amount == 0:
        print("Invalid Amount")
    else:
        print(f"Deposit: ${amount:,.2f}")
    
total_balance = initial_amount + sum(transactions)
print(f"Final Amount: ${total_balance:,.2f}")
print(f"Withdrawals: {count}")
