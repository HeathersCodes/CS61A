class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)


class C(B):
    def f(self, x):
        return x
a = A()
b = B(1)
b.n = 5
C(2).n #though we do not initialize c, we pass in b, C(2).y = 2, 
#and no f(x) in B class but in C, so C(2).z = 2 
#1st C instance then C class then B class so C(2).n == 4
a.z == C.z # -1 and find C.z in A class
#NOTES: B(1) is a instance not function
# Multiple Inheritance

class SavingsAccount(Account):
    """A bank account that charges for deposits."""

    deposit_fee = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)


class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    """A bank account that charges for everything."""

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1  # A free dollar!

supers = [c.__name__ for c in AsSeenOnTVAccount.mro()]
#['AsSeenOnTVAccount', 'CheckingAccount', 'SavingsAccount', 'Account', 'object']
