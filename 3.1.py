def area(a,b,c):
	p=(a+b+c)/2
	s= (p*((p-a)*(p-b)*(p-b)))**0.5
	return s 


a = float(input ('сторона треугольник 1:'))
b = float(input ('сторона треугольника 2:'))
c = float(input ('сторона треугольника 3:'))


print (area(a,b,c),'площадь треугольника')


