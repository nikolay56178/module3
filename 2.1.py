I=[1,4,1,6,'hello','a',5,'hello']
I_I=[]

for i in I:
	if I.count(i)> 1 and i not in I_I:
		I_I.append(i)
		
print('повторяющиеся элементы',I_I)		
