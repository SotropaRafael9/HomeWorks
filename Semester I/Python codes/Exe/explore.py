Number = int(input())
def oglindit(NumberThatIsChecked):
    ogl = 0 
    while NumberThatIsChecked:
        ogl = ogl *10 + n%10
        n/=10
    return ogl

while Number:
    LastDigit = Number % 10
    FirstDigit = Number
    while FirstDigit > 9:
        FirstDigit/= 10
    if (LastDigit + FirstDigit) != 9:
        print("Nu")
        break
    else:
        Number=Number/10
        oglindit(Number)
        Number/=10
        oglindit(Number)
if Number:
    print("DA")




