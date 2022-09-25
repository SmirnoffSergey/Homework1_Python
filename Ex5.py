# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Enter the coordinates X1 and Y1 of the first point A:')
x1 = float(input('X1 = '))
y1 = float(input('Y1 = '))
print()
print('Enter the coordinates X2 and Y2 of the second point B:')
x2 = float(input('X2 = '))
y2 = float(input('Y2 = '))
print()
distance = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)
print(f'Distance between two points A and B is: {distance}')