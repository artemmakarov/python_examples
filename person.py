class Person:
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay	
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay = int((1 + percent) * self.pay)	
	
bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay='100000')

if __name__ == '__main__':
	print (bob.name, bob.pay)
	print (sue.name, sue.pay)	
	print (bob.lastName(), sue.lastName())
	sue.giveRaise(2)
	print(sue.pay)