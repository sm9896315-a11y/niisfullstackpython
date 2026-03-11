class student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r 
		self.mark=m 
	def show(self):
		print("my name=",self.name)
		print("my roll no=",self.roll)
		print("my mark=",self.mark)

s1=student("seemoon",1,98)
s2=student("prabhu",2,97)
s1.show()
s2.show()				