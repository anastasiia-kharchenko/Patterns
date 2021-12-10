# Singleton Borg pattern
class Borg:

	# state shared by each instance
	__shared_state = dict()

	# constructor method
	def __init__(self):

		self.__dict__ = self.__shared_state
		self.state = 'Bank_analysis'

	def __str__(self):

		return self.state

# main method
if __name__ == "__main__":

	analyst = Borg() # object of class Borg
	manager = Borg() # object of class Borg
	creditor = Borg() # object of class Borg

	analyst.state = 'Analyst makes a report'
	# person1 changed the state
	print(analyst)
	# output --> Reports
	manager.state = 'Manager helps for people'
	# person2 changed the state
	print(manager)
	# output --> Help for people

	creditor.state = 'Creditor gives people money'
	# person3 changed the
	# the shared state
	print(creditor)  # output --> money for people



