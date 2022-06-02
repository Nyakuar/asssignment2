
class Bank:
    def __init__(self,name,number,balance,bankname) :
        self.name=name
        self.number=number
        self.balance=balance
        self.bankname=bankname


    def deposit(self,amount):
        self.balance+=amount
        return f"Hello your current balance is {self.balance}"

    def  withdraw(self,amount) :
        self.balance-=amount 
        return f"Hello your current balance is {self.balance}"    