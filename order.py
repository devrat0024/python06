size = input("what size pizza you want (S/M/L)?")
bill=0
if size == "S" or size == "s":
    bill += 100
    print("Small Pizza price is 100 Rs.")
elif size == "M" or size == "m":
    bill += 200
    print("Medium Pizza price is 200 Rs.")
else :
    bill += 300 
    print ("Large Pizza price is 300 Rs.")

add_pepperroni = input("Do you want to add (Y/N)?") 
if add_pepperroni == "Y" or add_pepperroni == "y":
    if size == "S" or size =="s":
        bill += 40
    else :
        bill += 60       
extra_cheese = input("Do you want to add (Y/N)?")
if extra_cheese == "Y" or extra_cheese == "y":
    bill += 80

print(f"your final bill is {bill}")