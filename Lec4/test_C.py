#  Решение задачи F
a_coeff = float(input())
b_coeff = float(input())
c_coeff = float(input())

if a_coeff != 0:
    # Значит решаем квадратное уравнение и
    # можем вычислять диксриминант
    discr = b_coeff ** 2 - 4*a_coeff*c_coeff
    if discr > 0:
        print("два корня")
    elif discr == 0:
        print("один корень")
    else:
        print("корней нет")
else:
    # Значит решаем линейное уравнение
    # Bx + C = 0
    #x = -c_coeff / b_coeff
    if b_coeff == 0:
        print("корней нет")
    else:
        print("один корень")