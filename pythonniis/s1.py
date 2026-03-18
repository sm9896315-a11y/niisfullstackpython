#display individual letter in forward
s="welcome"
for i in range(0,7,1): #(-7,0,1)
	print(s[i])
#or
s="welcome"
for i in range(0,len(s),1): #(-len(s),0,1)
	print(s[i])

	#display backward style
s="welcome"
for i in range(len(s)-1,-1,-1):   #(-1,len(s)-1,-1)
	print(s[i])

#or
s="welcome"
for i in range(6,0,-1):
	print(s[i])