from math import pi

def calculate_area(shape, dimension1, dimension2=0):
    match shape:
        case "circle":
            area = pi * dimension1 * dimension1
            print(area)
        case "rectangle":
            area = dimension1 * dimension2
            print(area)
        case "triangle":
            area = (dimension1 *  dimension2) / 2
            print(area)
    

calculate_area("triangle", 20 , 4)
calculate_area("circle", 14)
calculate_area("rectangle", 10, 10)
