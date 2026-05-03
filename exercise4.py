# Created a dictionary with different customers and printed it with a proper structure
customer = [
    {"name": "Sahil", "age": 21, "balance": 25000, "account_type": "Savings Account", "is_active": True },
    {"name": "Omar", "age": 20, "balance": 1500, "account_type": "Savings Account", "is_active": True },
    {"name": "Sajid", "age": 19, "balance": 100, "account_type": "Savings Account", "is_active": False }
]

def customer_summary(customer_list):
    for user in customer_list:
        print(f"Name is {user['name']} and {user['age']} years old with ${user['balance']:,.2f} in {user['account_type']}, is the account active: {user['is_active']}")

customer_summary(customer)
    


    

