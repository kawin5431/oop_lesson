class BankAccount:
    def __init__(self, account_number, account_type, account_name, init_balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.account_name = account_name
        self.balance = init_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depositing {amount} to {self.account_number}")
        else:
            print("Invalid deposit amount; must be greater than 0.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawing {amount} from {self.account_number}")
        else:
            print(f"Withdrawal amount {amount} exceeds the balance of {self.balance} for account {self.account_number}.")

    def show_account(self):
        print(f"Showing details for {self.account_number}")
        print({
            "account_number": self.account_number,
            "type": self.account_type,
            "account_name": self.account_name,
            "balance": self.balance
        })


class AccountDB:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        if self.search_account(account.account_number) is None:
            self.accounts.append(account)
            print(f"Account {account.account_number} added to database.")
        else:
            print(f"Account {account.account_number} already exists in the database.")

    def delete_account(self, account_number):
        account = self.search_account(account_number)
        if account:
            self.accounts.remove(account)
            print(f"Account {account_number} deleted from database.")
        else:
            print(f"{account_number} is an invalid account number; nothing to be deleted.")

    def search_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def get_all_accounts(self):
        return self.accounts


class Bank:
    def __init__(self):
        self.account_db = AccountDB()

    def create_account(self, account_number, account_type, account_name, init_balance=0):
        account = BankAccount(account_number, account_type, account_name, init_balance)
        self.account_db.add_account(account)

    def delete_account(self, account_number):
        self.account_db.delete_account(account_number)

    def deposit(self, account_number, amount):
        account = self.account_db.search_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print(f"{account_number} is an invalid account number; no deposit action performed.")

    def withdraw(self, account_number, amount):
        account = self.account_db.search_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(f"{account_number} is an invalid account number; no withdrawal action performed.")

    def show_account(self, account_number):
        account = self.account_db.search_account(account_number)
        if account:
            account.show_account()
        else:
            print(f"{account_number} is an invalid account number; nothing to be shown.")

    def show_all_accounts(self):
        for account in self.account_db.get_all_accounts():
            account.show_account()


bank = Bank()
bank.create_account("0000", "saving", "David Patterson", 1000)
bank.create_account("0001", "checking", "John Hennessy", 2000)
bank.create_account("0003", "saving", "Mark Hill", 3000)
bank.create_account("0004", "saving", "David Wood", 4000)
bank.create_account("0004", "saving", "David Wood", 4000)

bank.show_account('0003')
bank.deposit('0003', 50)
bank.show_account('0003')
bank.withdraw('0003', 25)
bank.show_account('0003')
bank.delete_account('0003')
bank.show_account('0003')
bank.deposit('0003', 50)
bank.withdraw('0001', 6000)


print("\nAll Accounts in Database:")
bank.show_all_accounts()

