class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)
    
accout1 = BankAccount(100, "kim", 15000)
print(accout1)