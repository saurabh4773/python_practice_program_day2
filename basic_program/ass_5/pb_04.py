# WAP to determine whether seller made a profit or loss

selling_amount = int(input("Enter the selling price of product : "))
actual_cost = int(input("Enter the actual cost of product : "))

diff = selling_amount - actual_cost
diff1 = actual_cost - selling_amount

if(diff > 0):
    print("Seller has made profit of :",diff)
elif(diff < 0):
    print("Seller has made loss of :",diff1)
else:
    print("Seller has nor made profit neither made loss")