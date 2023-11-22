def Prime(n):
    ok = True
    if n < 2 or (n > 2 and n % 2 ==0):
        ok = False 
    for i in range (2, n // 2):
        if n % i == 0:
            ok = False
    return ok
n = input("Pick a number: ")
n = int(n)
i = n
while not Prime(i):
    i+= 1
print (i)

