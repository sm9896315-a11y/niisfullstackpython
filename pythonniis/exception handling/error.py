print("main start")
try:
 	print(10//0)
 	print("try end")
except ZeroDivisionError as e :
	print(e)
print("end")