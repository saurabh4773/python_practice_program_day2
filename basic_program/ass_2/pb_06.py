''' WAP to assign different type of values to one variable 
at different instance of and print its type each time '''

my_list = [True, 12, 32.6, 'Hey', 74.46, False, 'What']

for i in range(0, len(my_list)):
    print(my_list[i],type(my_list[i]))