# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3

def drob(m, n):
    md = []
    for i in range(2, m):
        if m % i == 0:
            md.append(i)
    nd = []
    for i in range(2, n):
        if n % i == 0:
            nd.append(i)

    p = m
    q = n
    for i in range(0, len(md) + 1):
        for j in range(0, len(nd) + 1):
            if md[i] == nd[j]:
                p = int(p / md[i])
                q = int(q / nd[j])

    print(p, q)


drob(int(input()), int(input()))
