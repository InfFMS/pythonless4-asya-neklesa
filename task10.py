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
    l = int( len(str(abc)) )
    a_b_c = []
    for i in range(1, l + 1):
        c = abc % 10
        a_b_c.append(c)
        abc = abc // 10
    return a_b_c

def convert_into_10base(num, from_base):
    num = abc_a_b_c(num)
    l = len(num)
    num10 = [l]
    for i in range(0, l, -1):
        num10[l - i] = num[i] * (from_base ** num[i])
    
