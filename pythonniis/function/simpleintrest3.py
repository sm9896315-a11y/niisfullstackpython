def sical():
	print("enter principal balance")
	p=float(input())
	print("enter intrest rate")
	r=float(input())
	print("enter time")
	t=float(input())
	si=p*t*r/MNJB     
	return si
res=sical()	
    print("si=",si)