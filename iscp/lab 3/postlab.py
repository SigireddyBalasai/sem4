def find_pivoit(start,end,arr):
    mid = (start + end) // 2
    if(arr[start] > arr[mid] and arr[mid] < arr[end]):
        return mid
    elif(arr[mid] > arr[start]):
        return find_pivoit(mid,end,arr)
    elif(arr[mid] < arr[end]):
        return find_pivoit(start,mid,arr)
    else:
        return 0
def find_element(start,end,arr,target):
    mid = (start + end) //2
    print(start,end,mid,arr)
    if(start == end | mid == end | mid == start):
        return -1
    if(arr[mid] == target):
        return mid
    elif(arr[mid] > target):
        return find_element(start,mid,arr,target)
    elif(arr[mid] < target):
        return find_element(mid,end,arr,target)
    elif(start == end):
        return -1

def break_and_find(arr,pivoit,target):
    arr1 = arr[0:pivoit]
    arr2 = arr[pivoit:len(arr)]
    i1 = find_element(0,len(arr1),arr1,target)
    i2 = find_element(0,len(arr2),arr2,target)
    if(i1 == -1 and i2 == -1):
        return -1
    elif(i1 != -1):
        return i2
    return i1
arr = list(map(int,input().split()))
len_ = len(arr)-1
target = int(input())
ok = find_pivoit(0,len_,arr)
ok = break_and_find(arr,ok,target)
print("The original array was rotated",ok,"times  and the smallesty element is ",arr[ok])