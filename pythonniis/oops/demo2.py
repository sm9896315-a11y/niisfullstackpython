class student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r 
		self.mark=m 
	def show(self):
		print("my name=",self.name)
		print("my roll no=",self.roll)
		print("my mark=",self.mark)
	def update(self,n,r,m):
		self.__name=n
		self.__roll=r 
		self.__mark=m
	def set__Name(self,name):
		self.__name=name
	def set__Roll(self,roll):
		self.__roll=roll
	def set__Mark(self,mark):
		self.__mark=mark			
	def get__Name(self):
		return self.__name
	def get__Roll(self):
		return self.__roll
	def get__Mark(self):
		return self.__mark
s=student("seemoon",1,98)
s.show()
s.update("seemoon",2,40)
s.show()					