import json
data = {'test':'testpassword'}


def register(login,password):
	with open('reg.json','r',encoding='utf-8') as f:
		data = json.load(f)
	if login not in data.keys():
		data[login]=password
		with open('reg.json','w',encoding='utf-8') as f:
			json.dump(data,f)
		print ('регистрация успешна!')
		print(data)
	else:
	 	if login in data.keys():
				print ('Такой логин уже занят')

def login_function(login,password):
	with open('reg.json','r',encoding='utf-8') as f:
		data = json.load(f)
	if login in data.keys() and password in data.values():
		print('вход выполнен.')
	else:
		print ('неправильный логин или пароль')
		


while True:
	
	register_user = input('вход, выход или регистрация:')

	if register_user == 'выход':
		break

	elif register_user == 'вход':
		login_function(input('login:'),input('password:'))


	elif register_user == 'регистрация':
		register(input('login:'),input('password:'))


print('welcome')
	
		

	



