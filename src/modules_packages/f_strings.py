import datetime
from shapes.rectangular_cuboid import get_rectangular_cuboid_area
from geometry.area_rectangle import get_rectangle_area

dt_now = datetime.datetime.now()
print(f'неформатированная дата и время: {dt_now}')
print(f"форматированная дата и время: {dt_now:%d-%m-%Y %H:%M:%S}")

print (f'площадь прямоугольника со сторонами 1 и 2: {get_rectangle_area(1,2)}')
print (f'площадь прямоугольного параллелепипеда со сторонами 1 и 2, 3: {get_rectangular_cuboid_area(1,2,3)}')

