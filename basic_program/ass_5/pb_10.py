# WAP to accept coordinates and check whether in which quadrant it lies

x = float(input("Enter the X-coordinate : "))
y = float(input("Enter the Y-coordinate : "))

if(x > 0 and y > 0):
    print('(',x,',',y,')',"lies in first quadrant")
elif(x < 0 and y > 0):
    print('(',x,',',y,')',"lies in second quadrant")
elif(x < 0 and y < 0):
    print('(',x,',',y,')',"lies in third quadrant")
elif(x > 0 and y < 0):
    print('(',x,',',y,')',"lies in fourth quadrant")
elif(x == 0 and y == 0):
    print('(',x,',',y,')',"lies on centre")
elif(x == 0 and y > 0):
    print('(',x,',',y,')',"lies positive y-axis")
elif(x == 0 and y < 0):
    print('(',x,',',y,')',"lies on negative y-axis")
elif(x > 0 and y == 0):
    print('(',x,',',y,')',"lies on positive x-axis")
else:
    print('(',x,',',y,')',"lies on negative x-axis")