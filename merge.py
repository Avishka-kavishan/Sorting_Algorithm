def merge(arr):
    if len(arr)<=1:
        return arr
    else:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        merge(left) #recurtion
        merge(right) #recurtion

        x=0
        y=0
        z = 0 #index of the left,right,and merge array
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                arr[z] = left[x]
                x +=1
            else:
                arr[z] = right[y]
                y += 1
            z += 1

        while x < len(left):
            arr[z] = left[x]
            x +=1
            z +=1

        while y < len(right):
            arr[z] = right[y]
            y +=1
            z +=1

arr = [10,10,9,8,7,6,5,4,3,2,1,0]
merge(arr)
print(arr)
