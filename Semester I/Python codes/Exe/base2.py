n = input(int())
while n:
    u = n % 10
    p = 1
    if u % 2 == 0:
        u = u + 1
    nr = p*10 + u
    n/=10
print (nr)


