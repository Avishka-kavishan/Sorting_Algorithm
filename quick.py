def quick(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop(0)
        left = []
        right = []
        for item in arr:
            if item < pivot:
                left.append(item)
            else:
                right.append(item)
        return quick(left)+[pivot]+quick(right)
    
arr = [4,7,1,8,0,36,56,78]
print(quick(arr))