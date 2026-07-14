from geometry.area_rectangle import get_rectangle_area

def get_rectangular_cuboid_area(length, width, height):
    bottom = get_rectangle_area(length, width)   
    front = get_rectangle_area(length, height)   
    side = get_rectangle_area(width, height)
    
    total_area = 2 * (bottom + front + side)
    return total_area 