class BankAccount:
    def __init__(self, owner, starting_balance=0):
        self.__owner = owner
        self.__balance = max(0, starting_balance)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        
        try:
          if amount <= 0:
            return False
          self.__balance += amount
          return True
        except:
            return False

    def withdraw(self, amount):
        try:
          if amount <= 0 or amount > self.__balance:
            return False
          self.__balance -= amount
          return True
        except:
            return False
            
    def transfer_to(self, other_account, amount):
        try:
           if self.withdraw(amount) == True:
              other_account.deposit(amount)
              return True
           else:
              return False
        except: 
           return False
           

          
    
