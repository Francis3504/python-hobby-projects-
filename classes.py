class BankAccount:
    def __init__(self,name):
        self.name=name
        self.__balance=0
    def deposit(self,deposit):
        self._balance+=float(deposit)
    def withdraw(self,withdraw):
        if float(withdraw)<self.__balance:
            print(f"Your balance is {self.__balance-float(withdraw)}")
        else:
            print("Insufficient funds")
    
    def check_balance(self):
        print(f"balance is{self.__balance}")
account1=BankAccount("James")
print(account1.check_balance())