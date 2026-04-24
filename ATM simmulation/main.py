from account import Account
from transaction import Transaction
from atm import ATM

# Create account
user = Account("Amit", 1000)

# Transaction system
txn = Transaction()

# ATM system
atm = ATM(user, txn)

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance:", atm.show_balance())

    elif choice == "2":
        amt = int(input("Enter amount: "))
        print("New Balance:", atm.deposit(amt))

    elif choice == "3":
        amt = int(input("Enter amount: "))
        print(atm.withdraw(amt))

    elif choice == "4":
        print("\n--- STATEMENT ---")
        print(atm.get_statement())

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")