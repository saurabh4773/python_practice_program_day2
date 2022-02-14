# WAP to accept month number from user and print it's name and days in it

month = int(input("Enter the month number(1 to 12) : "))

if (month == 1):
    print("Name of month : January\nDays in it : 31")
elif(month == 2):
    print("Name of month : February\nDays in it : 28")
elif(month == 3):
    print("Name of month : March\nDays in it : 31")
elif(month == 4):
    print("Name of month : April\nDays in it : 30")
elif(month == 5):
    print("Name of month : May\nDays in it : 31")
elif(month == 6):
    print("Name of month : June\nDays in it : 30")
elif(month == 7):
    print("Name of month : July\nDays in it : 31")
elif(month == 8):
    print("Name of month : Auguest\nDays in it : 31")
elif(month == 9):
    print("Name of month : September\nDays in it : 30")
elif(month == 10):
    print("Name of month : October\nDays in it : 31")
elif(month == 11):
    print("Name of month : November\nDays in it : 30")
elif(month == 12):
    print("Name of month : December\nDays in it : 31")
else:
    print("Invalid month")