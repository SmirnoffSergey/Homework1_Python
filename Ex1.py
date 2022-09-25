# Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Enter the day of the week: ')
dayOfWeek = int(input())

while dayOfWeek < 1 or dayOfWeek > 7:
    print('Invalid day of the week. Please, try it again: ')
    dayOfWeek = int(input())
if dayOfWeek == 6 or dayOfWeek == 7:
    print('This is the day off!!!')
if dayOfWeek > 0 and dayOfWeek < 6:
    print('This is a weekday :(')
