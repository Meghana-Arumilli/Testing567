def my_brand(hw_assingment):
    import datetime
    name = "Meghana Arumilli"
    course = "Course 2023F-SSW567-A"
    pattern = "=*=*=*=%s=*=*=*="
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")


    print(pattern % name)
    print(pattern % course)
    print(pattern % hw_assingment)
    print(pattern % now)

my_brand('Hw 01')
print('')

import unittest

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        if (a*2 + b*2 == c*2) or (a*2 + c*2 == b*2) or (b*2 + c*2 == a*2):
            return "Isosceles and Right"
        else:
            return "Isosceles"
    elif a != b and b != c and a != c:
        if a*2 + b*2 == c*2 or a*2 + c*2 == b*2 or b*2 + c*2 == a*2:
            return "Scalene and Right"
        else:
            return "Scalene"