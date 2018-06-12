class Employee :
	"""docstring for ClassName"""
	def __init__(self, first, last, pay):
		self.first = first
		self.last  = last
		self.pay = pay
		self.email = first + '.' + last +'@company.com'
		
emp_1=Employee('Sachin', 'Tendulkar', 100000) #E1:Didn't Give sachin in quotes
emp_2=Employee('Virat', 'Kohli', 200000) #E2:written emp_1&2 under self that resulted in Indentation error

print(emp_1.first) #E3:Same as error2 written print statement under method,that resulted in indentation method
print(emp_2.first)