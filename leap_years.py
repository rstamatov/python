year = input("Year: ")
year = int(year)

if year % 4 == 0:   
    if year % 100 == 0:     
        if year % 400 == 0:
            print ("Leap year.")   
        else:
            print ("Not a leap year.")       
    else:
        print ("Leap year.")
        
else:
    print ("Not a leap year.")

############################################################################

if year % 4 != 0:
    print ("Not a leap year.")
elif year % 100 != 0:
    print ("Leap year.")
elif year % 400 != 0:
    print ("Not a leap year")
else:
    print ("Leap year.")


