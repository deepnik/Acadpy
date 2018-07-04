# Write a function to find factorial of a number but also store the factorials calculated in a dictionary.
def factorial(x):
    if x<=1:
        return 1
    else:
        f=x*factorial(x-1)
        return f
n=int(input("Enter a number: "))
fact= factorial(n)
print(fact)

c=factorial(n)
l=n
d={}
d[l]=c
print(d)
