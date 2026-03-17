from abc import*
class shape(ABC):
	def __init__(self,name):
		self.name=name
	@abstractmethod
	def perimeter(self):
		pass
class Rectangle(shape):
	def __init__(self,n,L,B):
		super().__init__(n)
		self.L=L
		self.B=B
	def perimeter(self):
		return 2*(self.L+self.B) 
class Square(shape):
	def __init__(self,n,L):
		super().__init__(n)
		self.L=L
	def perimeter(self):
			return 4*self.L 
r1=Rectangle("rect",6,8)
print(r1.perimeter())
s1=Square("sq",5)
print(s1.perimeter())	 