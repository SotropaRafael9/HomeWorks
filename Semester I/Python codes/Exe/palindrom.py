n = input("Choose a number: ")
n = int(n)
cn = n
ogl = 0
while cn > 0:
    c = cn % 10
    ogl = ogl *10 + c
    cn = cn // 10
if ogl == n:
    print (ogl,"is palindrom")
else:
    print("Is not palindrom")