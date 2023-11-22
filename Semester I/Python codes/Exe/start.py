mylist = [1 , 2, 3]
print (mylist)

print (mylist[1])

print (len(mylist))

print (len(mylist)-1)
print (mylist[-1])
 
x = mylist
print(mylist ,x)
x[1]='?'
print (mylist,x)

mylist = [1,2,3,4,5,6,7,8,9]
print (mylist[5:])
mylist[1:8]= "x"  
print(mylist)   

tup = 1, 2, 'a'
print (tup)
print (tup[2])

for e in tup:
        print (e)       

d = {'num': 1, 'den': 2}
print (d)

print (d['num'])

d['num']= 99
print (d['num'])

if 'den' in d:
        print ("We have num!")
del d['num']
if 'num' in d:
        print ("We have num!")
