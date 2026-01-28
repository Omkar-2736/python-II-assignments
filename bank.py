class BankAccount:
    def __init__(self, acc_no, bal):
        self.acc_no = acc_no
        self.bal = bal

    def deposit(self):
        amt = float(input("Enter amount to be deposited: "))
        self.balance = self.bal + amt
        print("Deposited:", amt)   

    def withdraw(self):
        amt = float(input("Enter amount to be withdrawn: "))
        if amt > self.bal:
            print("Insufficient balance")
        else:
            self.balance = self.bal - amt
            print("Withdrawn:", amt)

    def check_balance(self):
        print("Available balance:", self.bal)

if __name__ == "__main__":
    acc_no = input("Enter account number: ")
    bal = float(input("Enter initial balance: "))
    account = BankAccount(acc_no, bal)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account.deposit()
        elif choice == '2':
            account.withdraw()
        elif choice == '3':
            print(f"remaining balance is {account.bal - account.balance}")
            account.check_balance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
