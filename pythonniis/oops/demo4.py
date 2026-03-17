class Demo:
	def __init__(self,n):
		self.n=n
		print("constructor",self.n)
	def __init__(self):
		print("destructor",self.n)
d1=Demo("first")
print(id(d1))
d1=Demo("second")
print(id(d1))
d1=Demo("third")
print(id(d1))