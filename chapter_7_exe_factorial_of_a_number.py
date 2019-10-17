#exercise to use for loop to calculate the factorial of a positive number
number_1 = int(input('Enter a number to calculate factorial: '))
factorial = 1
print('The number entered is, ', number_1)
if number_1 < 0:
    print('The value is negative and no factorial is defined')
elif number_1 == 0:
    print('factorial is 1')
else:
    for number_1 in range (1, number_1 +1):
        factorial = factorial * number_1
    print('The factorial of', number_1, 'is', factorial)
