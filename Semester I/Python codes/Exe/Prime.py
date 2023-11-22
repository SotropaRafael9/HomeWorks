
x=input("Give me a number:")
x = int (x)
isPrime = True
##if x < 2 or (x > 2 and x % 2 ==0):
##       ok = False
for i in range (2, x // 2):
    if x % i == 0:
        isPrime = False
if isPrime == True:
    print("is prime")
else:
    print("is not prime") 