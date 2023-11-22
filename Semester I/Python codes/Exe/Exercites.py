def palindrom(n):
    ogl = 0
    cn = n
    while cn > 9:
        ogl = ogl *10 + cn % 10
        cn/=10
    if cn == n:
        return cn
palindrom()
