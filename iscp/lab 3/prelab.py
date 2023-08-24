class CeilAndFloor:
    def __init__(self,k : int,arr:list[int])->None:
        self.k = k
        self.arr = arr
    
    def floor(self)->int:
        if(min(self.arr) > self.k):
            return -1
        answer = -999
        for i in self.arr:
            if(i <= self.k and i >= answer):
                answer = i
        return answer
    
    def ceil(self)->int:
        if(self.k > max(self.arr)):
            return -1
        answer = 5000
        for i in self.arr:
            if(self.k <= i and i <= answer):
                answer = i
        return answer
n,k = list(map(int,input().split()))
array = list(map(int,input().split()))
cif = CeilAndFloor(k,array)
print(cif.ceil(),cif.floor())