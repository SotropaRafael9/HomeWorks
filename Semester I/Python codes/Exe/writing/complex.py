class Complex:
    _real: int = 0
    _imag :int = 0
    def __init__(self, real, imag) -> None:
        self._real = real
        self._imag = imag
    def __str__(self) -> str:
        return f"{self._real} + {self._imag}i"
    def __repr__(self) -> str:
        return str(self)
    def __eq__(self, __o: object) -> bool:
        return self._real == __o._real and self._imag == __o._imag
    
    def __ne__(self, __o: object) -> bool:
        return self._real != __o._real or self._imag != __o._imag

    def __add__(self, other):
        r= Complex(self._real+other._real, self._imag+other._imag)
        return r


q= Complex(1,2)
z = Complex(1, 2)
f = Complex(2,5)
print(z)
print("z.real")
print("z.imag")
print(z==q)
print(z==f)
print(z!=q)
print(z!=f)
print(z+q)

