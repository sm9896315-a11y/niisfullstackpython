print("enter the age")
x=int(input())
#print ("eligible") if x>=18 else print("not eligible")
msg="eligible" if x>=18 else "not eligible"
print(msg)

print("enter a no")
x=int(input())
#print ("even") if x%2==0 else print("odd")
msg="even" if x%2==0 else "odd"
print(msg)