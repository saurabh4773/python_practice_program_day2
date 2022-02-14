# WAP to calculate simple interest accept values from user

p = int(input("Enter the Principal Amount : "))
n = int(input("Enter the Time Period : "))
r = float(input("Enter the Rate Of Interest : "))

simple_interest = (p * n * r)/100
print("Simple Interest is : ",simple_interest)