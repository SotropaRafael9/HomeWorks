class L():
    def __init__(self,v=0,o=None) -> None:
        self.v=v
        self.o=o
    def __eq__(self, __o: object) -> bool:
        return self.v == __o.v and self.o == __o.o
a=L()
print(a==L())
a.n=L(1)
print(a==L())
print(a==L(0,L(1)))
