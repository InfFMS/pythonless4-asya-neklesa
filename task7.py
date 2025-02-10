# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.

def is_valid_triangle(side1, side2, side3):
    if side3 + side2 > side2 and side3 + side1 > side2 and side1 + side2 > side3:
        print(True)
        return True
    else:
        print(False)
        return False


is_valid_triangle(int(input()), int(input()), int(input()))
