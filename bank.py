
class Account:
    def __init__(self,name,number,) :
        self.name=name
        self.number=number
        # self.balance=balance
        self.deposits=[]
        self.withdrawal=[]
          
        # self.account=accountname

    def deposit(self,amount):
       
        if amount <=0: 
            return f" amount should be or less than zero"
        
        else:
            self.balance+=amount
            self.deposits.append(amount) 
              
            return f" you have deposited {amount}. your new balance is {self.balance}",self.deposits
    def  withdraw(self,amount) :
        # self.balance-=amount 
        if amount >self.balance :
            return f"your balance is {self.balance}, you cannot withdraw your balance is insuficient {amount}"
        elif amount <=0:
            return f"amount must be graeater eles: than zero "
        else:
            self.balance-=amount
            self.withdrawal.append(amount) 
            return f"you have withdrawn {amount} your balance is {self.balance}",self.withdrawal
        
    # def deposit_statement(self):
    #     print(*self.deposits,sep="\n")
            
    # def withdraw_statement(self):
    #     print(*self.deposits,self="\m")
        
    
    def deposit_Statement(self):
        for Statements in self.deposits:
            print(Statements)

    def withdraw_Statement(self):
        for statements in self.withdraw:
            print(statements)

    def current_balance(self):
        balance=self.balance
        print(balance)        
        
        