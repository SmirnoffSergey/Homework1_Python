# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

print('Enter the number of the quarter plane from 1 to 4:')
number_of_the_quarter = int(input())
print()

while number_of_the_quarter < 1 or number_of_the_quarter > 4:
    print('Enter the number of the quarter plane from 1 to 4:')
    number_of_the_quarter = int(input())

# Первый вариант решения

if number_of_the_quarter == 1: print('The coordinates by axes are: x > 0 and y > 0')
if number_of_the_quarter == 2: print('The coordinates by axes are: x < 0 and y > 0')
if number_of_the_quarter == 3: print('The coordinates by axes are: x < 0 and y < 0')
if number_of_the_quarter == 4: print('The coordinates by axes are: x > 0 and y < 0')

# Второй вариант решения

what_range = { 
    1: 'The coordinates by axes are: x > 0 and y > 0', 
    2: 'The coordinates by axes are: x < 0 and y > 0', 
    3: 'The coordinates by axes are: x < 0 and y < 0', 
    4: 'The coordinates by axes are: x > 0 and y < 0', 
} 
print(what_range[number_of_the_quarter])