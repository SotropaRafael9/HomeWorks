def Perfnum(x):
    s = 0
    for i in range(1,x-1):
        if x % i == 0:
            s = s + i
    if s == x:
        return x
n = input("Choose a number: ")
n = int(n)
i = n
while not Perfnum(i):
    i-=1
print (i)