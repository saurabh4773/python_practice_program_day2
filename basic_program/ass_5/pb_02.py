# WAP to find year is leap or not

year = int(input("Enter the year : "))

if (year % 400 == 0):
    print(year,"is a leap year")
elif(year % 4 == 0):
    print(year,"is a leap year")
elif(year % 10 == 0):
    print(year,"is not a leap year")
else:
    print(year,"is not a leap year")