import math

a = int(input('first number'))

b = int(input('second number'))

if math.gcd(a, b) > 1:

   print('взаимно простые')

else:

   print('не взаимно простые')
