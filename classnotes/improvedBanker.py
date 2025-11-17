def bank_account():
    from types import SimpleNamespace
    self = SimpleNamespace()
    balance = 0
    def deposit(amount):
        nonlocal balance
        balance += amount
        print(f"We now have {balance}")
    self.deposit = deposit
    return self

a1 = bank_account()
a2 = bank_account()
a1.deposit(15)
a1.deposit(15)
a2.deposit(2)
a2.deposit(2)
