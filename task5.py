# Напишите функцию, которая «переворачивает» число,
# то есть возвращает число, в котором цифры стоят в обратном порядке.
# Вводится натуральное число
# Пользоваться input()[::-1] запрещено!
# Идея задачи реализовать алгоритм,
# который будет работать для любого введенного натурального числа.

def pere(n):
    length = len(str(n))
    j = int(length)
    a = []
    for i in range(1, j + 1):
        x = n % 10
        n = n // 10
        a.append(x)
    print("".join((str(el) for el in a)))


pere(int(input()))
