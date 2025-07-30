nums=[2,5,7,8,9]
product=[]


for i in range(len(nums)):
      sum=1
      for j in range(len(nums)):
          if i!=j:
              sum=sum*nums[j]
      product.append(sum)
print(product)