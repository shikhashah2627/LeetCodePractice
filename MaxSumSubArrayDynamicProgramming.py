def maxSumSubArray(nums):
    maxSum = nums[0]
    sumList = []
    sumList.append(nums[0])
    for i in range(1,len(nums)-1):
        sumList.append(max(nums[i] , sumList[i-1] + nums[i]))
        maxSum = max(maxSum,sumList[i])
    return maxSum

a = [-2,-1,-3,-6,-4]
print(maxSumSubArray(a))


