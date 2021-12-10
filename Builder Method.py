# Abstract course
class Bank:

	def __init__(self):
		self.Report()
		self.operation()

	def Report(self):
		raise NotImplementedError

	def operation(self):
		raise NotImplementedError

	def __repr__(self):
		return 'Report : {0.report} | operations : {0.operations}'.format(self)

# concrete course
class Mono(Bank):

	"""Class for Data Structures and Algorithms"""

	def Report(self):
		self.Report = "finance"

	def operation(self):
		self.operation = "exchange"

	def __str__(self):
		return "Mono"

# concrete course
class Privat(Bank):

	"""Class for Software Development Engineer"""

	def Report(self):
		self.Report = "general"

	def operation(self):
		self.operation = "Credit"

	def __str__(self):
		return "Privat"

# concrete course
class Alfa(Bank):

	"""Class for Standard Template Library"""

	def Report(self):
		self.Report = "clients"

	def operation(self):
		self.operation = "Deposit"

	def __str__(self):
		return "Alfa"

# Complex Course
class ComplexBank:

	def __repr__(self):
		return 'Report : {0.Report} | operation: {0.operation}'.format(self)

# Complex course
class ComplexBank(ComplexBank):

	def Report(self):
		self.Report = "finance and general"

	def operation(self):
		self.operation = "exchange and credit"

# construct course
def construct_Bank(cls):

	Bank = cls()
	Bank.Report()
	Bank.operation()

	return Bank # return the course object

# main method
if __name__ == "__main__":

	Mono = Mono()
	# object for DSA course
	Privat = Privat()
	# object for SDE course
	Alfa = Alfa()
	# object for STL course

	complex_Bank = construct_Bank(ComplexBank)
	print(complex_Bank)
