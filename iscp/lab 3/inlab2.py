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
arr = list(map(int,input().split()))
len_ = len(arr)-1
ok = find_pivoit(0,len_,arr)
print("The original array was rotated",ok,"times  and the smallesty element is ",arr[ok])