class BankAccount(object):
  balance= 0
  def deposit(self, amount):
    self.balance =self.balance+ amount
  def withdraw(self, amount):
    if amount >self.balance:
      return "invalid transaction"
      

    self.balance = self.balance - amount
class MinimumBalanceAccount(BankAccount):
	MinimumBalanceAccount = 0