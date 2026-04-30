customer_name = "Omar"
customer_age = 23
account_balance = 1200
premium = input("Are you a premium customer? (y/n): ")

if premium.lower() == "y":
    print(f"{customer_name}, {customer_age} years old, with ${account_balance:,.2f} and is a premium customer")
    
elif premium.lower() == "n":
    print(f"{customer_name}, {customer_age} years old, with ${account_balance:,.2f} and is not a premium customer")

else:
    print("Invalid Option,Try again") 

