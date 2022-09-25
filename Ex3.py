# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Enter the coordinates X and Y of the point:')
x = float(input('X = '))
y = float(input('Y = '))

while x == 0 or y == 0:
    print('Invalid coordinate value. Please, try enter the coordinates other than 0.')
    x = float(input('X = '))
    y = float(input('Y = '))
print()

if x > 0: 
    if y > 0: 
        print('The point is in 1st quarter.') 
    else: 
        print('The point is in 4th quarter.') 
else: 
    if y > 0: 
        print('The point is in 2nd quarter.') 
    else: 
        print('The point is in 3rd quarter.')