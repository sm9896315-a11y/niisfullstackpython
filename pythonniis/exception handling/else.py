print("main start")
L=[10,20,30]
try:
	res(L[2]//2)
except:
	print("handel all exception")
else:
	print("else block",res)
print("main end")
#or
print("main start")
L=[10,20,30]
try:
	res(L[2]//0)
except:
	print("handel all exception")
else:
	print("else block",res)
print("main end")