def even_count_sum(n, arr, k):
    even_count = 0
    for i in range(n - k + 1):       # all subarrays of length k
        sub_sum = sum(arr[i:i+k])    # sum of k elements
        if sub_sum % 2 == 0:         # check if sum is even
            even_count += 1
    if even_count > 0:
        return even_count
    else:
        return -1

# Input
n = int(input("Enter n: "))
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

# Function call
print(even_count_sum(n, arr, k))
