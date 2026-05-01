initial_amount = 10000
transactions = [2000, -500, 3000, -1500, 4000, -2500, 3500, -1000]

def calculate_balance (initial_amount, transactions):
    return initial_amount + sum(transactions)
     
print(f"Final Amount: ${calculate_balance(initial_amount,transactions):,.2f}")

def count_withdrawals(transactions):
    count = 0
    for amount in transactions:
        if amount <0:
            count += 1
    return count

print(f"Amount of Withdrawals: {count_withdrawals(transactions)}")
        


    
