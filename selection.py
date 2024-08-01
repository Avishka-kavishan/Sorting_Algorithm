def selection(arr):
    for x in range(len (arr)):
        mint = x
        for y in range ( 1 , len(arr)):
            if arr[y] < arr[mint]:
                mint = y
        arr[y],arr[mint]=arr[mint],arr[y]
    return arr

arr= [10,10,9,8,7,6,5,4,3,2,1,0]
print(selection(arr))
