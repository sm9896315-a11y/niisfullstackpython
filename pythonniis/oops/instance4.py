class Demo:
	def __show(self):# private method
		print("hii")
	def disp(self): #public method
		self.__show()
ob=Demo()
ob.disp()  