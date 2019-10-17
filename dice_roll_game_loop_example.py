import random
min = 1
max = 6

roll_again = 'y'

while roll_again == 'y':
    print('rolling dice......')
    print('The values are....')
    dice_1 = random.randint(min, max)
    print(dice_1)
    dice_2 = random.randint(min, max)
    print(dice_2)
    roll_again = input('roll dice again?(y/n):')
