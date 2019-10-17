# this exercise is to check whether input is negative or positive
number = float(input('please enter a number'))
if number == 0:
    print('The value entered is zero')
if number < 0:
    print('The value entered is negative')
else:
    print('The number', number, 'is a positive value')
print('Bye, and until next time')

#testing if a number is odd or even
number_2 = int(input('Please enter a second number'))
if number_2%2 == 0:
    print(number_2, 'is an even number')
if number_2%2 != 0:
    print(number_2, 'is an odd number')
print('Bye for now')