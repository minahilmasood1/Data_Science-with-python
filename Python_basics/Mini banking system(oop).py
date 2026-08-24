import json
class BankAccount:
    def __init__(self,name, balance=0):
        self.name = name
        self.balance = balance
        self.deposit = 0
        self.withdraw = 0
        self.am_trans = 0
        self.oldpin = 0
    def __add__(self, deposit):
        self.deposit = deposit
        self.balance = self.balance + self.deposit
        return (f"{self.name} deposited ${self.deposit} amount.\nThe new amount is ${self.balance}")
        
    def __sub__(self, withdraw):
        self.withdraw = withdraw
        
        if self.withdraw <= self.balance:
            self.balance = self.balance - self.withdraw
            return (f"{self.name} withdrew ${self.withdraw} amount.")
        else:
            return("Insufficient balance to withdraw!")
        
    
    def transfer(self,acc_num,am_trans):
        self.am_trans = am_trans
        self.acc_num = acc_num
        if self.balance >= self.am_trans:
            return (f"${self.am_trans} tranfered to '{acc_num}'")
        else: return "Your balance is insufficient!"
    def history(self):
            self.x = (f"${self.deposit} deposited")
            self.y = (f"-${self.withdraw} withdrawn")
            self.z = (f"${self.am_trans} transferred")
            try:
                return list[self.x,self.y,self.z]
            except TypeError:
                if self.deposit == 0 and self.am_trans == 0:
                    return [self.y]
                elif self.withdraw == 0 and self.am_trans == 0:
                    return [self.x]
                elif self.deposit != 0 and self.am_trans != 0:
                    return [self.x,self.z]
                elif self.withdraw != 0 and self.am_trans !=0:
                    return [self.y, self.z]
    def update(self,oldpin):
        self.oldpin = oldpin
        self.abc = int(input("Write your old pin: "))
        if self.abc == self.oldpin:
            self.change = int(input("Write your new pin:"))
            print("password updated")
            
        else:
             print("Wrond credentials")
        try: 
            self.oldpin = self.change
        except AttributeError:
            self.oldpin = oldpin
    def acc_balance(self):
        self.pin = int(input("Write your pin to see your balance: "))
        if self.pin == self.oldpin:
            return self.balance
        else:
            return ("Wrong pin!")
        
object_1 = BankAccount("Minahil",200)
print(object_1.__sub__(100))

print(object_1.transfer(12345,2300))
print(object_1.history())
object_1.update(1234)
print(object_1.acc_balance())
