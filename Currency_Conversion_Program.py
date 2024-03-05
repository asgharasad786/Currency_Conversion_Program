print("\nWelcome to the World of Currency Conversion.\n\n1.Dollar to Pkr\n2.Pkr to Dollar\n3.UK dollar to Pkr\n4.Pkr to UK Dollar\n5.Euro to Pkr\n6.Pkr to Euro")
x = int(input("\nEnter your choice: "))

if x == 1: 
    # currency conversion Dollar to PKR  
    x = 279.65
    y = int(input("\nEnter the amount in Dollars: "))
    z = x * y
    print("\nYour amount in rupees is:", z)
elif x == 2:
    # currency conversion PKR to Dollar
    x = 279.65
    y = int(input("\nEnter the amount in Rupees: "))
    z = y / x
    print("\nYour amount in Dollar is:", z)
elif x == 3:
    # currency conversion UK Dollar to PKR
    x = 352.28
    y = int(input("\nEnter the amount in UK Dollar: "))
    z = x * y
    print("\nYour amount in PKR is:", z)
elif x == 4:
    # currency conversion PKR to UK Dollar
    x = 352.28
    y = int(input("\nEnter the amount in Rupees: "))
    z = y / x
    print("\nYour amount in Dollar is:", z) 
elif x == 5:
    # currency conversion Euro to PKR
    x = 303.31
    y = int(input("\nEnter the amount in Euro: "))
    z = x * y
    print("\nYour amount in PKR is:", z)
elif x == 6:
    # currency conversion PKR to Euro
    x = 303.31
    y = int(input("\nEnter the amount in Rupees: "))
    z = y / x
    print("\nYour amount in Euro is:", z)
elif x == 7:
    # currency conversion PKR to Qatari Riyal
    x = 76.77
    y = int(input("\nEnter the amount in Rupees: "))
    z = y / x
    print("\nYour amount in Qatari Riyal is:", z) 
elif x == 8:
    # currency conversion Qatari Riyal to PKR
    x = 76.77
    y = int(input("\nEnter the amount in Qatari Riyal: "))
    z = x * y
    print("\nYour amount in PKR is:", z)    
else:
    print("Invalid entry")
