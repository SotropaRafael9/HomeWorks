NumberThatIsChecked = int(input())
FirstTwinNumber = 0
SecoundTwinNumber = 0

def isPrime(NumberThatIsChecked: int):    ## x = Parameter who  
    isPrime = True
    if NumberThatIsChecked < 2 or (NumberThatIsChecked > 2 and NumberThatIsChecked % 2 == 0):
        isPrime = False
    for Divider in range (3, NumberThatIsChecked // 2, 2):
        if NumberThatIsChecked % Divider == 0:
            isPrime = False
    return isPrime

Index = NumberThatIsChecked + 1
while SecoundTwinNumber == 0:
    if isPrime(Index):
        FirstTwinNumber = Index
        Index+= 2
        if isPrime(Index):
            SecoundTwinn = Index
            break
    Index = Index + 1
print (FirstTwinNumber," ", SecoundTwinNumber)


 