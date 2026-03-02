def check(no):
	if no%2==0:
		return "even"
	else:	
		return "odd"
print("enter a no")
no=int(input())
print(check(no))