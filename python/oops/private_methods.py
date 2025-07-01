class account:
    def __init__(self,account_no,account_passwrd):
        self.account_no=account_no
        self.__account_passwrd=account_passwrd

    def get_pass(self):
        print(self.__account_passwrd)

c=account(20000,2435)
print(c.account_no)
c.get_pass()