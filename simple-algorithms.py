#
# Author:        Emem-Akeabasi Andy
#
# Created:       29/01/2021
# Purpose:       Simple Algorithms Application
# Copyright:     (c) Emem Andy 2021
#
#---------------------------------------------------------------------------


x = 0

while x < 31:
    x += 1
    if (x % 3 == 0) and (x % 5 == 0) and (x % 15 == 0):
        print('x is currently:',x)
        print('FizzBuzz\n')
    elif (x % 3) == 0:
        print('x is currently:',x)
        print('Fizz\n')
    elif (x % 5) == 0:
        print('x is currently:',x)
        print('Buzz\n')
    else:
        continue
print('ALL DONE!!!')       