print(2**3**2)
print(10*4//3)
print(10//3*4)

a=10
print(id(a),a)
a=20
print(id(a),a)


a=10
b=2.5
c="hi"
print(a,b,c)

a,b,c=1,4.9,"hey"
print(a,b,c)

a=34,"tq",6.9
print(a)
print(type(a))

a=10
b=230
a,b=b,a
print(a,b)

a=12
b=45
c=67
print("before swapping a=",a, "b=",b, "c=",c )
d=c
c=b
b=a 
a=d 
print("after swapping a=",a, "b=",b, "c=",c )


a=10
b=4
c=a--b
print(c)

a=4
a+=1
print(a)

print(3==3)

print("x" in "hello")
print(46 in [10,67,90,46])

a=[10]
b=[10]
c=[20]
print(a is b)
print(a is not c)