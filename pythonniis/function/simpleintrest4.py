def sical(p,t,r):
	si=p*t*r/100
	return si 
print("enter principal balance")
p=float(input())
print("enter intrest rate")
r=float(input())
print("enter time")
t=float(input())
res=sical(p,t,r)
print("si=",si)