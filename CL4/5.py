 #A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will 
#cost 100. Judge and print total cost for user.

units=int(input("enter the number of unit you want to purchase : "))
cost=100*units
if cost>=1000:
	dis=cost/10
	print("you are eligible for discount of %d and your total cost is : %d "\
	%(dis,cost-dis))
else:
	print("your total cost is : "+str(cost))
