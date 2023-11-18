class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} dollars. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} dollars. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

# インスタンスの作成
account1 = BankAccount(owner="John Doe", balance=1000)

# 操作例
account1.deposit(500)
account1.withdraw(200)
print(f"Current balance: {account1.get_balance()} dollars")
