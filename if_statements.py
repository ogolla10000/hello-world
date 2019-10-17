#these exercises cover the work in chapter 6 dealing with if control statement
users_age = int(input('What is your age: '))
if users_age > 0:
    print('We hope you have enjoyed', users_age,'years under the sun')
    print('The square of your age is:', users_age**2)
print('See you soon')

#this section demonstrates the use of the else
if users_age < 0:
    print('This character has not seen the sun yet')
else:
    print('We hope you have enjoyed', users_age,'years under the sun')
print('That is all for now')

#this section demonstrates the elif statement
#the elif comes after the if, but before the else statements
#each elif represents a condition to be executed if the prior condition was not
amount_in_account = float(input('How much money do you have in your account? '))
if amount_in_account == 0:
    print('Sorry you do not have any funds in your account')
elif amount_in_account < 500:
    print('Your account has',amount_in_account,'shillings and you may be soon running out of funds')
elif amount_in_account < 1000:
    print('Your account has', amount_in_account, 'shillings. This is living on the edge')
elif amount_in_account < 10000:
    print('You have', amount_in_account, 'shillings in your account Sir, this is a tidy sum')
elif amount_in_account < 1000000:
    print('You have', amount_in_account,'shillings in your account, you are a rich man')
else:
    print('Good day Sir/Maam, how may we be of assistance today?')
#this part demonstrates the use of the 'nested if'
#the nested if allows for the execution of another if statement within another
snowing = bool(input('Is it snowing outside?'))
temperature = int(input('What does the temperature feel like today? '))
if temperature < 0:
    print('It is freezing')
    if snowing:
        print('Put on your boots')
    print('Time for a hot chocolate')
elif temperature < 5:
    print('It may rain today and you still need to keep warm')
elif temperature < 15:
    print('The day looks up you may survive without a sweater')
elif temperature < 25:
    print('It will be a warm summer day today, wear bright :-)')
else:
    print('Just make a plan to go to the pool today, the weather is good for a swim')
print('Bye and till next time')
#if expressions
status = ('teenager' if users_age > 12 and users_age < 20 else 'not teenages')
print(status)