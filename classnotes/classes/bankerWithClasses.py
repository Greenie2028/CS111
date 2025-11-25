class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def open_account(self, name):
        new_account = BankAccount.CreateNew(name)
        self.accounts[new_account.number] = new_account
class BankAccount:
    def __init__(self, name, account_num, balance=0):
        self.name = name
        self.account_num = account_num
        self.balance = balance
    def CreateNew(self,name):
        from random import randint
        return BankAccount(name, randint(10000,99999))

    def __str__(self):
        return f"{self.name}, {self.balance}"

    def deposit(self, amount):
        self.balance += amount

    def transfer(fromAccount, toAccount, amount):
        fromAccount.balance -= amount
        toAccount.balance += amount
    def __gt__(self,other):
        return self.balance > other.balance

a1 = BankAccount("Levi Clements", 9867)
a2 = BankAccount("Other Person", 12345)
#BankAccount.deposit(a1, 5) == a1.deposit(5)
a1.deposit(20001)
a1.transfer(a2, 10000)
if a1 > a2:
    print("a1 is bigger than a2")
else:
    print("It is not greater than")