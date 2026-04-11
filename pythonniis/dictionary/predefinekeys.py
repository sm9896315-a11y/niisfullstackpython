#predefined functions dict keys
d={1:"a",2:"b",3:"c",4:"d"}
print(d.keys())

d={1:"a",2:"f",3:"e"}
for i in d.keys(): 
	print(i,d[i])

d={1:"a",2:"f",3:"e"}
for k ,v in d.items():
	print(k,v)