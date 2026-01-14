password = 'a123456'
enter_code = input('pls enter the password: ')
x = 0
while x < 3:
	if enter_code == password:
		print('login sucessfully')
		break
	else:
		x = x + 1
		y = 4 -x
		print('you still', y, 'times change')
		enter_code = input('pls enter the password: ')

if x >= 3: print('you try too many times!!')