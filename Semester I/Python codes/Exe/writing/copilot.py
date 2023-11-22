class SparceMatrix:
    listn = []
    def __init__(self, m, n) -> None:
        self._m = m
        self._n = n
    
    def get(self, x, y):
        if x < 0 or x > self._n or y < 0 or y >self._m:
            raise ValueError("out of matrix")
        for i in self.listn:
            if i[0] == x and i[1] == y:
                return i[2]
        return 0
    
    def set(self, x, y, z):
        if x < 0 or x > self._n or y < 0 or y >self._m:
            raise ValueError("out of matrix")
        for i in self.listn:
            if i[0] == x and i[1] == y:
                i[2] = z
        self.listn.append([x,y,z])
    
    def __str__(self) -> str:
        rez = ""
        for i in range (0,self._n):
            for j in range (0,self._m):
                rez += str(self.get(i, j)) + " "
            rez += "\n"
        return rez
    
    def __getitem__(self, index):
        return self.listn[index]
    

            
        






#  0 0 0
#  0 1 0
#  0 2 3

m1 = SparceMatrix(3, 3)
m1.set(1, 1, 3)
print(m1)
try:
    m1.set(3,3,99)
except Exception as e:
    print(type(e))

m1.set(1, 1, m1.get(1, 1)+1)
print(m1)
print(m1[0])
