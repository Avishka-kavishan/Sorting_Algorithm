from functools import reduce
def radix (arr,num_digit):
    for digit in range(num_digit):
        buckets = [[] for x in range (10)]
        for num in arr:
            bucket_index = (num // (10 ** digit) )% 10
            buckets [bucket_index].append(num)
        arr = reduce (lambda y,z : y+z , buckets)
    return arr
    
number = [4,7,1,8,0,36,56,78]
num_digit = len(str(max(number)))
print(radix(number,num_digit))

