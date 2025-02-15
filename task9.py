# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!

def degre2(n)
    count = 0
    while n % 2 == 0:
        n = n // 2
        count +=  1
    if n == 1:
        print("yes")
    else:
        print("no")

def degree2(n):
    while n % 2 == 0:
        n /= 2
        return n
    return degree(n)

degre2( int(input()) )
if degree2( int(input()) ) == 1:
    print('yes')
else:
    print('no')
