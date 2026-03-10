# ATM System with Multiple Accounts

# Dictionary storing multiple accounts
accounts = {
    "1001": {"name": "Rahul", "pin": "1234", "balance": 5000},
    "1002": {"name": "Priya", "pin": "5678", "balance": 8000},
    "1003": {"name": "Amit", "pin": "4321", "balance": 10000}
}

# Function to check balance
def check_balance(account):
    print(f"💰 Available Balance: ₹{account['balance']}\n")


# Function to deposit money
def deposit(account):
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        account["balance"] += amount
        print("✅ Amount deposited successfully!\n")
    else:
        print("❌ Invalid amount!\n")


# Function to withdraw money
def withdraw(account):
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print("✅ Please collect your cash.\n")
    else:
        print("❌ Insufficient balance!\n")


# ATM Menu
def atm_menu(account):
    while True:
        print("===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance(account)
        elif choice == "2":
            deposit(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            print("🙏 Thank you for using ATM!\n")
            break
        else:
            print("❌ Invalid choice!\n")


# Main Program
def main():
    print("===== WELCOME TO ATM =====")
    
    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print(f"\nWelcome {accounts[acc_no]['name']}!\n")
        atm_menu(accounts[acc_no])
    else:
        print("❌ Invalid Account Number or PIN!")


# Run program
if __name__ == "__main__":
    main()