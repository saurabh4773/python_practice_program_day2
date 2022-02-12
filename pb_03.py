''' program for drawing pyramids of * '''

def pyramid(size):
    dist = (size*2)-2
    for i in range(0,size):
        for j in range(0,dist):
            print(end=" ")
        dist = dist - 1
        for j in range(0,i+1):
            print("*",end=" ")
        print(" ")

def right_pyramid(size):
    dist = (size*2)-2
    for i in range(0,size):
        for j in range(0,dist):
            print(end="")
        dist = dist - 1
        for j in range(0,i+1):
            print("*",end="")
        print(" ")

def left_pyramid(size):
    dist = (size*2)-2
    for i in range(0,size):
        for j in range(0,dist):
            print(end=" ")
        dist = dist - 1
        for j in range(0,i+1):
            print("*",end="")
        print(" ")

while True:
    print("Menu \n1.Pyramid \n2.Right Pyramid \n3.Left Pyramid \n4.Exit")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        size = int(input("Enter the pyramid length you want : "))
        pyramid(size)

    elif choice == 2:
        size = int(input("Enter the pyramid length you want : "))
        right_pyramid(size)

    elif choice == 3:
        size = int(input("Enter the pyramid length you want : "))
        left_pyramid(size)

    elif choice == 4:
        break

    else:
        print("Invalid !")