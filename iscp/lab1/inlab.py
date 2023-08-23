class Stack(list):
    def __init__(self):
        self.stack = []
    def push(self,data : int) -> None:
        self.stack.append(data)
    def pop(self):
        try:
            return self.stack.pop()
        except:
            return None
def cummulative_sum(array:list):
    list_2 = []
    ok = 0
    for i in range(len(array)):
        list_2.append(ok+array[i])
        ok += array[i]
    return list_2
list_1 = [1,2,1,1]
list_1.reverse()
list_2 = [1,1,2]
list_2.reverse()
list_3 = [1,1]
list_3.reverse()
l1 = cummulative_sum(list_1)
l2 = cummulative_sum(list_2)
l3 = cummulative_sum(list_3)
for i in l1:
    try:
        i1 = l1.find(i)
        i2 = l2.find(i)
        l3 = l3.find(i)
        
    