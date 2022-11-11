# 2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
1.
x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))

if not (x or y or z) == (not x and not y and not z):
    print(True)
else:
    print(False)
    
    
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(not (x or y or z) == (not x and not y and not z))
#             print(x, y, z)
