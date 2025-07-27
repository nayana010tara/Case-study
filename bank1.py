# Bank Account Manager

# Step b: Use variables and data types
account_holder = "Nayana"
account_number = "123456789"
balance = 0.0

# Step d: Use functions to perform deposit, withdrawal, and balance inquiry
def deposit(amount):
    global balance
    balance += amount
    print(f"₹{amount} deposited. New balance: ₹{balance:.2f}")

def withdraw(amount):
    global balance
    # Step c: Conditional check for sufficient balance
    if amount <= balance:
        balance -= amount
        print(f"₹{amount} withdrawn. New balance: ₹{balance:.2f}")
    else:
        print("Insufficient balance. Withdrawal failed.")

def check_balance():
    print(f"Current balance: ₹{balance:.2f}")

# Step a: Simulate the operations
def bank_operations():
    while True:
        print("\n----- Bank Account Manager -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amt = float(input("Enter amount to deposit: ₹"))
            deposit(amt)
        elif choice == "2":
            amt = float(input("Enter amount to withdraw: ₹"))
            withdraw(amt)
        elif choice == "3":
            check_balance()
        elif choice == "4":
            print("Thank you for using the Bank Account Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the simulation
bank_operations()
