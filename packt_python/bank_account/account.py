class Account:

    def __init__(self,filepath): #is the instantiation function that sets the filepath
        self.path = filepath
        with open(filepath, "r") as file: #opens the file in read mode
            self.balance = int(file.read()) #this allows the file to be read as an integer
    
    def withdraw(self,amount): #takes the balance and subtracts the amount, creating a new balance
        self.balance = self.balance - amount
        
    def deposit(self,amount): #adds the amount to the balance
        self.balance = self.balance + amount
    
    def commit(self): #
        with open(self.path, 'w') as file:
            file.write(str(self.balance))
    
'''account = Account("balance.txt") #or "bank_account//balance.txt" if you don't want to change directory in the terminal
print(account.balance)
account.withdraw(1)
print(account.balance)
account.deposit(12)
print(account.balance)
account.commit()'''

class Checking_Account(Account): #is an inheritance class, or a sub class
    """This is a doc string"""

    type="this is a class variable" #data member

    def __init__(self, filepath, fee): #calls __init__() function from the Account class; is a constructor; is an instantiation
        Account.__init__(self, filepath)
        self.fee = fee #data member
    
    def transfer(self, amount): #this is a method
        self.balance = self.balance - amount - self.fee
    
checking = Checking_Account("balance.txt", 2)
#checking.deposit(1000)
checking.transfer(20)
print(checking.balance)
checking.commit()

print(checking.__doc__) #prints the doc string

#You can create multiple of these last few lines
#Just change the file directory and you can get values of different accounts