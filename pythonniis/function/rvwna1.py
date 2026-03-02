def check():
	print("enter a no")
	no=int(input())
	if no%2==0:
		return True
	else:	
		return False
if check():
	print("even")
else:
	print("odd")	


def check():
	print("enter a no")
	no=int(input())
	if no%2==0:
		return "even no"
	else:	
		return "odd no"
print(check())	


def check():
	print("enter a no")
	no=int(input())
	if no%2==0:
		return 0
	else:	
		return 1
if check()==0:
	print("even")
else:
	print("odd")