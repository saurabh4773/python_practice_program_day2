# WAP to calculate surface area and volume of a cylinder

r = float(input("Enter the radius of cylinder : "))
h = float(input("Enter the height of cylinder : "))

area_cylinder = 2 * 3.14 * r * (h+r)
volume_cylinder = 3.14 * h * r * r

print("Surface Area of Cylinder is :",area_cylinder)
print("Volume of Cylinder is :",volume_cylinder)
