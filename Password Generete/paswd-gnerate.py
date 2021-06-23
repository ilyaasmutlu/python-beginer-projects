import random

print('''
Password Generator
==================

''')

chars = 'qwertyuiopasdfghjklzxcvbnm,QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&&**(),./;[]123456789'

number = input('number of passwords?')
number = int(number)

lenght = input('password length: ')
lenght = int(lenght)

print('\nhere are your passwords:\n')

for pwd in range(number):
    password =''
    for c in range(lenght):
        password += random.choice(chars)
    print(password)