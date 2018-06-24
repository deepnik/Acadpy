
#Points	Prize
#1-50	    No Prize
#51-150	    Wooden Dog
#151-180	Book
#181-200	Chocolates

n1=int(input("Enter a value: "))
print("\n")
print("You Entered : ",n1)
print("\n")
if n1>=1 and n1<=50:
 print("No Prize")
elif n1>50 and n1<=150:
 print("Wooden Dog") 
elif n1>150 and n1<=180:
 print("Book")
elif n1>180 and n1<=200:
 print("Chocolates") 
else:
 print("Sorry! No Prize this time.") 
