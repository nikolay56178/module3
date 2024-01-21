from random import randint

n=3
m=[[randint(0,100) for i in range(n)] for j in range (n)]

print (m)

c = []
for l in m:
    c.append(max(l))

print(max(c))