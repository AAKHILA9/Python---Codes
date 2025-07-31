nums = [1, 12, -5, -6, 50, 3]
k = 4
ans = float('-inf') 

for i in range(len(nums) - k + 1):
    summ = sum(nums[i:i + k])    
    average = summ / k            
    ans = max(ans, average)       

print(ans)
