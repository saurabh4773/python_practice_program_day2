# WAP to check triangle is valid or not

angle_1 = float(input("Enter the first angle : "))
angle_2 = float(input("Enter the second angle : "))
angle_3 = float(input("Enter the third angle : "))

sum_of_angles = angle_1 + angle_2 + angle_3

if(sum_of_angles != 180):
    print("Triangle is Invalid")
elif(angle_1 == 0):
    print("Triangle is Invalid")
elif(angle_2 == 0):
    print("Triangle is Invalid")
elif(angle_3 == 0):
    print("Triangle is Invalid")
else:
    print("Triangle is Valid")