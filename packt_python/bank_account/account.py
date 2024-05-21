class Account:

    def __init__(self,filepath):
        self.path = filepath
        with open(filepath, "r") as file:
            self.balance = int(file.read())
    
    def withdraw(self,amount):
        self.balance = self.balance - amount
        
    def deposit(self,amount):
        self.balance = self.balance + amount
    
    def commit(self):
        with open(self.path, 'w') as file:
            file.write(str(self.balance))
    
account = Account("balance.txt") #or "bank_account//balance.txt" if you don't want to change directory in the terminal
print(account.balance)
account.withdraw(1)
print(account.balance)
account.deposit(12)
print(account.balance)
account.commit()
