# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = input('X = ')
y = input('Y = ')
z = input('Z = ')
left_side = not (x or y or z)
right_side = (not x) and (not y) and (not z)
print(left_side == right_side)