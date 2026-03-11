class Demo:
	def __init__(self,x,y):#method
		self.__x=x #private instance variable
		self.__y=y
	def show(self):
		print(ob.__x)
		print(ob.__y)
ob=Demo(4,8)
ob.show()
