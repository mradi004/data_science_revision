class account:
    def __init__(self,balance,acc):
        self.balance=balance
        self.acc=acc

    def debit(self,amount):
        self.balance -= amount
        print(f"you account is debited with {amount} current balace is {self.balance}")

    def credited(self,amount):
        self.balance+=amount
        print(f"your account is credited with {amount} current balance is {self.balance}")

acc1=account(20000,23456)
acc1.debit(5000)
acc1.credited(3000)
print(acc1.balance)                