country = input('where are you from: ')
age = input('what is your age: ')
age = int(age) #casting change from string to integer
if country == 'Hongkong':
	if age >= 18:
		print('you can take driving examination')
	else: 
		print('you are not qualified for the driving examination')
elif country == 'America':
	if age >= 16:
		print('you can take driving examination')
	else: 
		print('you are not qualified for the driving examination')