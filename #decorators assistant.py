#decorators assistant
#assuming carpet tiles are 1 square unit, 1 roll of wallpaper is 10 square units and 1 litre of paint is 10 square units
#subroutines
def get_user_inputs():
    l = int(input("enter length"))
    b = int(input("enter breadth"))
    h = int(input("enter height"))
    return l, b ,h

def calculate_area(length, breadth, height):
    floor = length*breadth
    wall = breadth*height*2 + length*height*2
    return floor, wall

def calculate_requirements(floor_area, wall_area):
    ct = floor_area/1
    wp = wall_area/10
    paint = floor_area/10
    return ct, wp, paint

def display_results(carpet_tiles, wallpaper, paint_litres):
    print("You need", carpet_tiles, " carpet tiles,", wallpaper, "rolls of wallpaper and ",paint_litres, "litres of paint")
#main program

length, breadth, height = get_user_inputs()
floor_area, wall_area =calculate_area(length, breadth, height)
carpet_tiles, wallpaper, paint_litres = calculate_requirements(floor_area, wall_area)
display_results(carpet_tiles, wallpaper, paint_litres)

#psuedocode
"""
1.enter the length, breadth and height of a rectangular room
2.calculate the floor area and wall area
3.calculate
    the number of carpet tiles for the floor
    the number of rolls of wallpaper for the walls
    the number of litres of paint for the ceiling
4.display the results of these calculations


1.1. Ask user to enter length of room and store response in length
1.2. Ask user to enter the breadth of room and store response in breadth
1.3. Ask user to enter the height of the room and store response in height
1.4. Return length, breadth and height to main program

2.1. Calculate floor area by multiplying length and breadth
2.2. Calculate wall area by multiplying length and height, multiplying this by two, then adding the result of multiplying breadth and height times two
2.3. Return floor area and wall area to main program

3.1. Set width of carpet tile to 0.5cm
3.2. Set roll coverage to 10m^2
3.3. Set paint coverage to 5m^2
3.4. Calculate no of carpet tiles needed by dividing floor area by width of carpet tile squared
3.5. Calculate no rolls wallpaper by dividing wall area by roll coverage
3.6. Calculate litres of paint needed by dividing floor area by paint coverage
3.7. Return no of carpet tiles, no rolls wallpaper and litres paint to main program

4.1. Display the length, breadth and height the user entered
4.2. Display the calculated floor area
4.3. Display the calculated wall area
4.4. Display the number of carpet tiles needed
4.5. Display the number of rolls of wallpaper needed
4.6. Display the number of litres of paint needed




"""