''' Write a menu written program
        area of circle
        area of rectangle
        area of triangle
        area of square
 '''

print("****MENU****\n1.Area of circle\n2.Area of rectangle\n3.Area of triangle\n4.Area of square")
choice = int(input("Enter your choice : "))

if choice == 1:
    r = float(input("Enter the radius of circle : "))
    area_circle = 3.14 * r * r
    print("Area of circle is",area_circle)

elif choice == 2:
    len = float(input("Enter the length of rectangle : "))
    breadth = float(input("Enter the breadth of rectangle : "))
    area_rectangle = len * breadth
    print("Area of rectangle is",area_rectangle)

elif choice == 3:
    base = float(input("Enter the base of triangle : "))
    height = float(input("Enter the height of triangle : "))
    area_triangle = base * height * 1/2
    print("Area of triangle is",area_triangle)

elif choice == 4:
    length = float(input("Enter the length of side of square : "))
    area_square = length ** 2
    print("Area of square is",area_square)

else:
    print("Invalid choice !")