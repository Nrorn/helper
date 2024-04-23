#Напишите программу на Python, которая решает квадратное уравнение вида ax^2 + bx + c = 0. Программа должна принимать значения a, b и c от пользователя и выводить корни уравнения. 
# import math

# def solve_quadratic_equation(a, b, c):
#     # Вычисляем дискриминант
#     discriminant = b**2 - 4*a*c

#     # Проверяем знак дискриминанта
#     if discriminant > 0:
#         # Два действительных корня
#         x1 = (-b + math.sqrt(discriminant)) / (2*a)
#         x2 = (-b - math.sqrt(discriminant)) / (2*a)
#         return x1, x2
#     elif discriminant == 0:
#         # Один корень (корень кратности два)
#         x = -b / (2*a)
#         return x,
#     else:
#         # Два комплексных корня
#         real_part = -b / (2*a)
#         imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
#         return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)

# def main():
#     # Получаем значения a, b и c от пользователя
#     a = float(input("Введите значение a: "))
#     b = float(input("Введите значение b: "))
#     c = float(input("Введите значение c: "))

#     # Решаем уравнение
#     roots = solve_quadratic_equation(a, b, c)

#     # Выводим результат
#     print("Корни уравнения:")
#     for root in roots:
#         print(root)

# if __name__ == "__main__":
#     main()


import math

def solve_quadratic_equation(a, b, c):
    # Вычисляем дискриминант
    discriminant = b**2 - 4*a*c

    # Проверяем значение дискриминанта
    if discriminant > 0:
        # Уравнение имеет два различных корня
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
    elif discriminant == 0:
        # Уравнение имеет один корень
        x = -b / (2*a)
        return x
    else:
        # Уравнение не имеет действительных корней
        return None

# Запрашиваем значения a, b и c у пользователя
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

# Решаем уравнение
solution = solve_quadratic_equation(a, b, c)

# Выводим результат
if solution is None:
    print("Уравнение не имеет действительных корней")
elif isinstance(solution, tuple):
    print("Уравнение имеет два различных корня:", solution)
else:
    print("Уравнение имеет один корень:", solution)