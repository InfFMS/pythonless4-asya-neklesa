# Напишите функцию convert_base(num, from_base, to_base),
# которая переводит натуральное число num из системы
# счисления с основанием from_base в систему счисления
# с основанием to_base
# 2 ≤ to_base ≤ 36 ; 2 ≤ from_base ≤ 36
# На входе три числа num, from_base, to_base
# На выходе одно число - результат работы функции
# Подсказка (если не получается решить):
# Попробуйте разбить задачу на две подзадачи:
# перевод из десятичной системы счисления в любую
# перевод из любой системы счисления в десятичную
# Объедините эти две подзадачи, получите ответ.

def abc_a_b_c(abc):
#числа в цифры
    l = int( len(str(abc)) )
    a_b_c = []
    for i in range(1, l + 1):
        c = abc % 10
        a_b_c.append(c)
        abc = abc // 10
    return a_b_c
#число перевернуто


def a_b_c_abc(a_b_c):
    l = int(len(a_b_c))
    abc = ''
    for i in range(0, l):
        abc += str(a_b_c[i])
    abc = int(abc)
    return abc


def convert_into_10base(num, from_base):
    if from_base != 10:
        num = abc_a_b_c(num)
        l = len(num)
        num_10 = [0]*l
        num10 = 0
        for i in range(0, l):
            num_10[i] = num[i] * (from_base ** i)
            num10 += num_10[i]
        num10 = a_b_c_abc(num10)
    else:
        num10 = a_b_c_abc(num)
    print(num10)
    return num10


def convert_from_10base(num, to_base):
    if to_base != 10:
        num = a_b_c_abc(num)
        numx = []
        i = 0
        while num > 0:
            numx.append(num % (to_base))
            i += 1
            num = num // to_base
        numx = a_b_c_abc(numx)
    else:
        numx = a_b_c_abc(num)
    print(numx)
    return numx


num = int(input())
from_base = int(input())
to_base = int(input())
convert_from_10base(convert_into_10base(num, from_base), to_base)
