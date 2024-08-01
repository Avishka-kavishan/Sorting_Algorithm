def bucket_sort(array):

  # Find the maximum and minimum values in the array
  max_val = max(array)
  min_val = min(array)

  # Calculate the range and number of buckets
  range_val = max_val - min_val
  num_buckets = int((max_val + min_val)/2)
  print(num_buckets)

  # Create empty buckets
  buckets = [[] for a in range(num_buckets)]

  # Distribute elements into buckets
  for num in array:
    index = int((num - min_val) * (num_buckets - 1) / range_val)
    buckets[index].append(num)

  # Sort elements within each bucket
  for bucket in buckets:
    bucket.sort()

  # Concatenate the sorted buckets
  sorted_array = []
  for bucket in buckets:
    sorted_array.extend(bucket)

  return sorted_array

# Example usage
array = [10,10,9,8,7,6,5,4,3,2,1,0]
sorted_array = bucket_sort(array)
print(sorted_array)
