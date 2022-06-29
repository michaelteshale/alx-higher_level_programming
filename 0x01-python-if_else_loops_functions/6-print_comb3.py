#!/usr/bin/python3
for num in range(0, 10):
    for num2 in range(num + 1, 10):
        if num != num1:
            print('{}'.format(num), end='')
        if num == 8 and num1 == 9:
            print('{}'.format(num1))
        else:
            print('{}, '.format(num1), end='')
