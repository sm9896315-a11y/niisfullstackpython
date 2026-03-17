from abc import*
class shape(ABC):
	def __init__(self,name):
		self.name=name
	@abstractmethod
	def area(self):
		pass
class Triangle(shape):
	def __init__(self,n,L,B):
		super().__init__(n)
		self.L=L
		self.B=B
	def area(self):
		return 1/2*self.L*self.B 
r1=Triangle("tri",6,8)
print(r1.area())
