def isPrime(NumberThatIsChecked : int):
    IsPrime = True
    if NumberThatIsChecked < 2 or (NumberThatIsChecked > 2 and NumberThatIsChecked % 2 ==0):
        IsPrime = False
    for i in range(3, NumberThatIsChecked // 2, 2):
        if NumberThatIsChecked % i == 0:
            IsPrime = False
    return IsPrime
NumberThatIsChecked = int(input("Choose a number: "))
Index = 2
Sum = 0 
while Index < NumberThatIsChecked:
    Sum = 0
    if isPrime(Index):  
        Sum = Sum + Index
        if isPrime(NumberThatIsChecked - Sum):
            print (Index,NumberThatIsChecked - Sum)
    Index+= 1



    
