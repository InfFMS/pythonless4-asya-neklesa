# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!

def degree2(n):
    if n == 1:
        print('yes')
    elif n % 2 == 1:
        print('no')
    else:
        return degree2(n // 2)


degree2( int(input()) )
