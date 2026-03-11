#1 object creation
class Demo:
	def __init__(self,x,y):
		self.x=x
		self.y=y
print("Enter 2 values")
ob=Demo(int(input()),int(input()))
print("Display first object values")
print(ob.x,ob.y)