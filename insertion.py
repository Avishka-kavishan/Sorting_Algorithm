def insertion(arr):
    for i in range(1,len(arr)):
        sorted = arr[i]
        d = i #index of i 
        while d>0 and sorted<arr[d-1]:
            arr[d] = arr[d-1]
            d -=1
        arr[d] = sorted
    return arr

arr = [4,7,1,8,0,36,56,78]
print(insertion(arr))