# WAP to determine if a given number is armstrong or not

num = int(input("Enter the number : "))
temp = num
sum = 0
while temp > 0:
    n = temp % 10
    sum = sum + n**3
    temp = temp//10

if(num == sum):
    print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong number")