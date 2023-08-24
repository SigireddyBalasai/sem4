class StockSpanner:
    def __init__(self):
        self.arr = []
        self.solu = []
    def next(self,n):
        count = 1
        self.arr.append(n)
        for i in range(len(self.arr)):
            if(self.arr[i] < n):
                count += 1
        print(count)
        self.solu.append(count)
        return count

    def __str__(self):
        return ",".join(list(map(str,self.solu)))

input_command = list(map(int,input().split()))
ok = StockSpanner()
for i in input_command:
    ok.next(i)
print(ok)

        
