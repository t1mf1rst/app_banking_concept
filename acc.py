class Account:
	"""docstring for Account - oop principles used"""
	def __init__(self, filepath):
		super(Account, self).__init__()
		self.filepath = filepath
		with open(self.filepath, 'r') as file:
			self.balance = int( file.read() )

	def withdraw(self, amount):
		self.balance = self.balance - amount

	def deposit(self, amount):
		self.balance = self.balance + amount

	def commit(self):
		with open(self.filepath, 'w') as file:
			file.write(str(self.balance))

class Checking(Account):
	""" class inherited from Account class """
	def __init__(self, filepath, fee):
		Account.__init__(self, filepath)
		self.fee = fee
	
	def transfer(self, amount):
		self.balance = self.balance - amount - self.fee

checking = Checking("balance.txt", 1)

checking.transfer(130)
print(checking.balance)
checking.commit()