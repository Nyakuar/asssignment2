from datetime import datetime
from itertools import count
class Account:
    def __init__(self,accountname,accountnumber):
        self.accountname = accountname
        self.accountnumber = accountnumber
        self.balance = 0 
        self.deposits = []
        self.withdrawals = []
        self.transaction_fee = 100
        self.loan = 0
        self.statement = []
    
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit must be positive"
        else: 
            self.balance+=amount
            now = datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"you have deposited"
            }  
            self.deposits.append(amount)   
            self.statement.append(transaction)
            return f"Hello {self.accountname} Your balance is {self.balance} your deposits is {self.deposits}"  
                    

    def withdraw(self,amount):
        if amount+self.transaction_fee>self.balance:
            return f"Hello {self.accountname} Your balance is {self.balance} you can't withdraw {amount}"
        elif amount<=0:
            return f"Hello {self.accountname} The amount should be positive" 
        else:       
            self.balance-=amount+self.transaction_fee
            now = datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"you have withdrawn"
            }
            self.withdrawals.append(amount)
            self.statement.append(transaction)
            return f"Hello, {self.accountname} your new balance is {self.balance} and your withdrawals are {self.withdrawals} {self.statement}"

    def borrow(self,amount):         
            count = sum(self.deposits)
            limit = count*(1/3)
            interest=amount*0.03
            if amount<=100:
                return "Loan must be more than 100"  
            elif self.loan>0:
                return f"Loan denied, kindly repay your current loan of {self.loan}"
            elif len(self.deposits)<10:
                return "your deposits must be at least more than 10"

            elif amount>=limit:
                return f"You have reached your limit, your loan of {amount} is denied "
  
            elif amount>=self.balance:
                return f"Dear customer you can't borrow that money is lower than a limit of" 
            else:
                 self.loan+=amount
                 self.loan+=interest
                 now= datetime.now()
                 transaction={
                    "amount":amount,
                    "time":now,
                    "Narration":"you have borrowed"
                }
                 self.statement.append(transaction)
                 return f"Hello {self.accountname} your loan of {amount} has been approved and your interest is {interest} you will pay back {self.loan}" 
    
    def repay(self,amount):
    
        if amount<0:
            return f"Dear customer your payment is too low"
        elif amount<=self.loan:
            paid = self.loan - amount
            return f"Dear customer you have  paid {amount} and your loan balance is {paid} "
        else:
            payment=amount-self.loan
            self.balance+=payment

            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"you have repaid your loan"
            }
            self.statement.append(transaction)

            return f"Dear customer {self.accountname} you have fully paid your loan and the overpay of {payment} is added on your account, your new balance is {self.balance}"
    
    def transfer(self,account_instance,amount):

        Total= amount + self.transaction_fee
        if amount<0:
            return f"Dear customer {self.accountname} your amount is too low"
        elif Total>self.balance:
            return f"Dear customer {self.accountname} you balance is {self.balance} and you need atleast {Total}"
        else:
            self.balance-=Total
            return f"Dear customer you  have sent {amount} to {account_instance} your current balance is {self.balance}"                       

    def deposits_statement(self,amount):
        if amount<0:
            for deposit in self.statement:
                return deposit   

    def withdrawals_statement(self):
        for withdrawal in self.statement:
            return withdrawal  
    def current_balance(self):
        return self.balance   
    def full_statement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Narration= transaction["Narration"]
            time= transaction["time"]
            date= time.strftime("%x %X")
            print(f"{date}: {Narration} {amount}")
            
account = Account(accountname="Nyakuar",accountnumber=58943)
print(account.deposit(500))
print(account.deposit(500))
print(account.deposit(1000))
print(account.deposit(1000))
print(account.withdraw(200))
print(account.transfer("Gesare",2000))
# print(account.transfer("Gesare",1000))





















































