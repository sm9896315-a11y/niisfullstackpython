class student:
	def __init__(self,name):
		self.__name =  name
	@property
	def name(self):                     #getter
		return self.__name

	@name.setter
	def name(self,value):               #setter
		self.__name = value
s = student("sushree")
print(s.name)
s.name = "Saswati"

print(s.name)