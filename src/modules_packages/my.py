from shapes.rectangular_cuboid import get_rectangular_cuboid_area

length = int(input('введите длину стороны прямоугольного параллелепипеда:'))
width = int(input('введите ширину стороны прямоугольного параллелепипеда:'))
height = int(input('введите высоту стороны прямоугольного параллелепипеда:'))
print(f'Площадь прямоугольного параллелепипеда равна {get_rectangular_cuboid_area(length, width, height)}')