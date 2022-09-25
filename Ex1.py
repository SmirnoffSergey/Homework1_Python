# Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Enter the day of the week:')
day_of_the_week = int(input())
print()

while day_of_the_week < 1 or day_of_the_week > 7:
    print('Invalid day of the week. Please, try it again: ')
    day_of_the_week = int(input())
if day_of_the_week in (6, 7):
    print('This is the day off!!!')
else:
    print('This is a weekday :(')