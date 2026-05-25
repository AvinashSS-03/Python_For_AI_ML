nums=[1,2,3,4,5]
print(nums[::-1]) #slicing method
n=len(nums)
for i in range(n-1,-1,-1):#range(start from last index,go till last element 0,step by -1 that means move backwards)
    print(nums[i])   #for loop for reversing
