# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять
n = int(input())
def number_to_words(n):
    d = ['','десять','двадцать','тридцать','сорок','пятьдесят', 'шестьдесят','семьдесят','восемдесят','девяносто']
    e = ['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять']
    u = ['одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнацать']
    if 10 < n < 20:
        for i in range(1, 10):
            if n%10 == i:
                print(u[i])
    else:
        print(d[n//10] + ' ' + e[n%10])

