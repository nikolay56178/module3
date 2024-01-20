number = int(input('Введите целое число\nчтобы узнать сумму цифр этого числа'))
sum_number = 0
while number >0:
	i = number % 10
	sum_number += i
	number //= 10

print ('сумма цифр введенного числа:',sum_number)
