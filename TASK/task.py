    # 1. Напишите программу, которая принимает на вход цифру,
    # обозначающую день недели, и проверяет, является ли этот день выходным.

# day = int(input("Введите число дня недели от 1 до 7: "))

# if day < 1 or day > 7:
#     print("Неверное число")
# elif day > 5:
#     print("Выходной день!")
# else:
#     print("Рабочий день!")


    # 2. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# x = 0
# y = 1
# left = not (x or y)
# right = not x and not y
# statement = left == right
# print (statement)

    # 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
    # причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка

# x = int(input('Введите число x≠0:'))
# y = int(input('Введите число y≠0:'))
# if x > 0 and y > 0:
#     print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 1 ')
# elif x < 0 and y > 0:
#     print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 2 ')
# elif x < 0 and y < 0:
#     print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 3 ')
# elif x > 0 and y < 0:
#     print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 4 ')

    # 4. Напишите программу, которая по заданному номеру четверти,
    # показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int(input('Введите номер четверти: '))
# if n < 1 or n > 4:
#     print('Пожалуйста, повторите ввод')
# # elif n == 1:
#     print('x > 0 and y > 0')
# elif n == 2:
#     print('x < 0 and y > 0')
# elif n == 3:
#     print('x < 0 and y < 0')
# elif n == 4:
#     print('x > 0 and y < 0')

    # 5. Напишите программу, которая принимает на вход координаты двух точек
    # и находит расстояние между ними в 2D пространстве

# ax = float(input('Введите координаты точки a по оси x:'))
# ay = float(input('Введите координаты точки a по оси y:'))
# bx = float(input('Введите координаты точки b по оси x:'))
# by = float(input('Введите координаты точки b по оси y:'))

# import math
# distans = math.sqrt((ax-bx)**2+(ay-by)**2)
# print(f'Растояние между точкой A до точки B = {distans}' )