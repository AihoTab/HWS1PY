# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input())
p_inf = float('inf')
n_inf = float('-inf')
if a == 1:
    print(f'Х {0, p_inf} Y {0, p_inf}')
elif a == 2:
    print(f'Х {0, n_inf} Y {0, p_inf}')
elif a == 3:
    print(f'Х {0, n_inf} Y {0, n_inf}')
elif a == 4:
    print(f'Х от {0} до {p_inf} Y {0, n_inf}')
else:
    print('Введено неверное значение')
