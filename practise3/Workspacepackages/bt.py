class BankAccount:
    def __init__(self,accountNumber, accountName=None):
        self.accountNumber=accountNumber
        self.accountName= accountName
        self.balance=0
    def getAccountNumber(self):
        return self.accountNumber
    def getAccountName(self):
        return self.accountName
    def getBalance(self):
        return self.balance
    def deposit(self,money):
        self.balance=self.balance+money
    def withdraw(self,money):
        if money <= self.balance:
            self.balance=self.balance-money
            return True
        else:
            return False

class Bank(BankAccount):
    def __init__(self, listBankAccount): #listBankAccount is dictionary, Name must be typed with quotes
        self.list=eval(listBankAccount) 
        
    def search(self,accountNumber):
        return self.list.get(accountNumber, -1)
    def getTotal(self):
        return self.balance
    def getItem(self,accountNumber):
        if accountNumber in self.list.keys():
            return BankAccount(accountNumber)
    def addAccount(self, accountNumber, accountName):
        if accountNumber in self.list.keys():
            return False
        else:
            self.list[accountNumber]=f'{accountName}'
    def depositMoney(self, accountNumber, money):
        if accountNumber in self.list.keys():
            super().deposit(accountNumber,money)
            return True
        else:
            return False
    def withdrawMoney(self,accountNumber, money):
        super().withdraw(accountNumber,money)        
    def removeAccount(self,accountNumber):
        if accountNumber in self.list.keys():
            self.list.pop(accountNumber)
            return True
        else:
            return False

        
        
        
        
        