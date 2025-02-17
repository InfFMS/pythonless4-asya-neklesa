# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.

def nod(a,b):
    v = []
    if a < b:
        a, b = b, a
    for i in range (1, a):
        if a % i == 0 and b % i == 0:
            v.append(i)


    print('НОД:', max(v))

nod( int(input()),int(input()) )

