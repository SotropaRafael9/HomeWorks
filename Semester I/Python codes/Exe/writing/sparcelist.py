class SparceList:
    listn = []
    def __init__(self, length) -> None:
        self._length = length
    
    def __getitem__(self, index):
        if index <0 or index > self._length:
            raise ValueError("out of list")
        for i in self.listn:
            if i[0] == index:
                return i[1]
        return 0
    
    def __setitem__(self, index, value):
        if index <0 or index > self._length:
            raise ValueError("out of list")
        for i in self.listn:
            if i[0] == index:
                i[1] = value
                return
        self.listn.append([index, value])
    
    def __str__(self) -> str:
        rez=""
        for i in range(0, self._length):
            rez+= str(self[i]) + " "
        return rez  
    
    def __len__(self):
        return len(self.listn)








l=SparceList(10)
l[0]=1
l[5]=7
try:
    l[17]=20
except Exception as e:
    print(type(e))
# for el in l:
#     print(el[0], el[1])
print(l)
print(len(l))
# for el in l[1,5]:
#     print(el)