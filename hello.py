name = input('What is your name?')
month = input ('What month were you born in?')

#count number of letters in name
nameLength = len(name)


print('Hello ' + name)
print('There are ' + str(nameLength) + ' in your name')
if month == 'January':
	print('It is your birthday month!')
elif month != 'January':
	print('Your birthday is in ' + month)