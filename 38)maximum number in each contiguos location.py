nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
maxx = []

for i in range(len(nums)-k+1):
    subarray=nums[i:i+k]
    maxi=max(subarray)
    maxx.append(maxi)
print("maximum number in each contigious location is:",maxx)

