class employee:
	def __init__(self, first, last, pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+'.'+last+'@company.com'
emp_1 = employee('corey','schafer',50000)
emp_2= employee('test', 'user', 60000)
#emp_1.first = input("")

print ("Emplpyee 1 is:",emp_1.first," ",emp_1.last,"he/she earns: ",emp_1.pay,)
print ("The email address is generated as follows: ",emp_1.email)

class pinnumber:
	def __init__(self, first_name, last_name):
		self.first=first_name
		self.last=last_name
	
