# python function to print fibonacci series

def fibonacci_series(a,b,n):
    print(a, b, sep="\n")
    while n-2:
        c = a + b
        a,b = b,c
        print(c)
        n = n - 1

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
n = int(input("How many elements do you want in a series : "))

fibonacci_series(a,b,n)