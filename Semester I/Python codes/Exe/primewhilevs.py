from operator import truediv


x = input("Give me a number: ")
x = int(x)

isPrime = True
i = 2
while isPrime and i <= x // 2:
    i+= 1
    if x % i == 0: 
        isPrime = False
if isPrime:
    print("is prime")
else:
    print ("is not prime")

