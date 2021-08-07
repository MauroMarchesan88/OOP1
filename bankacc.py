class account:
  def set_details(self,name,balance=0):
    self.name = name
    self.balance = balance

  def display(self):
    print(self.name,self.balance)
    
  def withdraw(self,amount):
    self.balance -= amount

  def deposit(self,amount):
    self.balance += amount

acc1 = account()
acc2 = account()

acc1.set_details('juan', 1000)
acc2.set_details('bob', 2000)

acc1.display()
acc2.display()

acc1.deposit(1500)
acc1.withdraw(1000)
acc2.deposit(1700)
acc2.withdraw(600)

acc1.display()
acc2.display()
