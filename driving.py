country = input('where are you from: ')
age = input('what is your age: ')
age = int(age) #casting 
if country == 'Hongkong':
	if age >= 18:
		print('you can take driving examination')
	else: 
		print('you are not qualified for the driving examination')
