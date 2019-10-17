#exercise to practice working with the different number Types
print('Welcome, this program will help you convert Km into miles')
km_given = int(input('How many Km would you like to convert into miles? '))
if km_given < 0:
    print('This is a negative value and cannot be converted')
else:
    print(km_given, 'km converts to', km_given / (0.6214), 'miles')
print('now you know')