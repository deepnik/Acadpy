# Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a
#program that determines and prints all the perfect numbers between 1 and 1000. [An integer number is said to be
#“perfect number”if its factors, including 1(but not the number itself), sum to the number.
#E.g., 6 is a perfect number because 6=1+2+3].

def perfect(n):
	sum=0
	for i in range(1,n):
		if n%i==0:
			sum=sum+i
	if sum==n:
		print(n,"is a perfect number")
for x in range(1,1001):
	perfect(x)
