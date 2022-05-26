#Each obj has its own local state
#Each obj also know how to manage its own local state, based on method calls
#Method calls are messages passed between obj
# A class serves as a template for its instances
#assignment and def statement in suite create attributes
#obj construction: when a class is called: a new instance of class is created
#the  __init__ (constructor) methods of the class is called with the new obj as its 1st argument( named self)
#along with additional argu provided by call expr

#binding an obj to a new name using assignment does not create a new obj

class Account:
    """An account has a balance and a holder.
    All accounts share a common interest rate.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> Account.interest = 0.04
    >>> a.interest
    0.04
    """

    interest = 0.02  # A class attribute 
    #class attributes are shared across all instances of a class, cuz they are attribute of class

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount): #self is a name refer to instance, we are changing the balance of particular account
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount): # their names are bound as attributes of the class
                                # dot notation automatically supplies the 1st argu to method
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
#obj receive messages via dot notation
#dot notation accesses attributes of the instance or its class
#combound operator with dot expr
#attribute of calss or of instance
# obj + function = Bound Method
# <expr>.<name> instancds attibutes 1st then class attribute then bound method
