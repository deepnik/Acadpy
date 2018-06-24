#From a list containing ints, strings and floats, make three lists to store them
l=[1,'a',5,'d',4.5,'r',5.3,48,52,2.6,7.5,'e','f']
i=[]
c=[]
f=[]
for x in l:
        if type(x)==int:
            i.append(x)
        elif type(x)==str:
            c.append(x)
        elif type(x)==float:
            f.append(x)
print('the list is:',l)
print('the list is:',i)
print('the list is:',c)
print('the list is:',f)
