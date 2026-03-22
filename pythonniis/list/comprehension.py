L=[5,8,6,7,9,5,11,7,6]
L1=[i for i in L]
print(L1)
L=[4,8,7]
L1=[i+3 for i in L]
print(L1)
L=[5,9,4,6]
L1=[i+3 for i in L if i%2==0]
print(L1)
L=[5,8,6,7,12,9,3]
L=[i for i in L if i%2==0]
print(L)