class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn {amount} using overdraft facility")
        else:
            print("Overdraft limit exceeded")



savings = SavingsAccount("Pratham", 5000, 5)
savings.display_balance()
savings.deposit(2000)
savings.add_interest()
savings.withdraw(3000)
savings.display_balance()

print("---------------")

current = CurrentAccount("Rahul", 3000, 2000)
current.display_balance()
current.deposit(1000)
current.withdraw_with_overdraft(5500)
current.display_balance()
