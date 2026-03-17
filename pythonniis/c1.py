class A:
	def f1(self):
		print("A is a person")
class B(A):
	def f2(self):
		print("A is a student")
class C(B):
	def f3(self):
		print("A is an engineeringstudent")
ob=C()
ob.f1()
ob.f2()
ob.f3()