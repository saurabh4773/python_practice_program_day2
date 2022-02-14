# categorize person depending on their height

person_height = int(input("Enter the height of the person : "))

if(person_height < 150):
    print("Dwarf")
elif(person_height == 150):
    print("Average heighted")
elif(person_height >= 165):
    print("Tall")
else:
    print("Average")