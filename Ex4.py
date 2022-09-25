# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

print('Enter the number of the quarter plane from 1 to 4:')
numberQuarter = int(input())
print()

while numberQuarter < 1 or numberQuarter > 4:
    print('Enter the number of the quarter plane from 1 to 4:')
    numberQuarter = int(input())
print()

if numberQuarter == 1: print('The coordinates by axes are: x > 0 and y > 0')
if numberQuarter == 2: print('The coordinates by axes are: x < 0 and y > 0')
if numberQuarter == 3: print('The coordinates by axes are: x < 0 and y < 0')
if numberQuarter == 4: print('The coordinates by axes are: x > 0 and y < 0')