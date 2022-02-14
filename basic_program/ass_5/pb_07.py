# WAP to check whether candidate is eligible for voting or not

candidate_age = int(input("Enter the Age of candidate : "))

if(candidate_age >= 18):
    print("This candidate is eligible for voting")
else:
    a = 18 - candidate_age
    print("This candidate is not eligible for voting, candidate is eligible for voting after",a,"years")