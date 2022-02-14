# WAP to accept marital status and print miss and mrs in front of name

name = input("Enter your name : ")
marry_status = input("Are you married (y/n) : ")
gender = input("Enter your gender (female/male) : ")

if(marry_status == 'y' and gender == 'female'):
    print("Mrs.",name)
elif(marry_status == 'n' and gender == 'female'):
    print("Miss.",name)
elif(marry_status == 'y' and gender == 'male'):
    print("Mr.",name)
elif(marry_status == 'n' and gender == 'male'):
    print("mister.",name)
else:
    print("Invalid Choices")