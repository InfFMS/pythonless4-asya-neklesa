# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7

def min_prime(n):
    if n != 1:
        m = 0
        for i in range(2, n + 1):
            if n % i == 0:
                m = i
                break
        if n//m != 1:
            return str(m) + "*" + str(min_prime(n//m))
        else:
            return str(m)
    return ""

print(min_prime( int(input()) ))


# def prime_numbers(n):
#     p = []
#     for i in range(2, int(n ** 0.5 + 2)):
#         count = 0
#         if n % i == 0:
#             count += 1
#         if count == 1:
#             p.append(i)
#
#     return p
#
#
# def pmn(n):
#     p = prime_numbers(n)
#     mn = []
#     for i in range(0, len(p)):
#         while n % p[i] == 0:
#             mn.append(p[i])
#             n = n//p[i]
#     print("*".join((str(el) for el in mn)))
#
#
# pmn(int(input()))

