def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	print("factorial=",f)
print("enter a no")
no=int(input())
facttest(no)
